from collections import defaultdict

def if_contains_anagrams(str_list):
    """
  Checks if there are at least 91 pairs of anagrams in a list of strings.

  Args:
    str_list: A list of strings.

  Returns:
    True if there are at least 91 pairs of anagrams, False otherwise.
  """
    str_dict = defaultdict(list)
    for word in str_list:
        str_dict[tuple(sorted(word.lower()))].append(word)
    anagram_count = 0
    for group in str_dict.values():
        n = len(group)
        anagram_count += n * (n - 1) // 2
    return anagram_count >= 91