from collections import Counter

def if_contains_anagrams(str_list):
    """
  Check if there are at most 19 pairs of anagrams in a list of strings.

  Args:
    str_list: A list of strings.

  Returns:
    True if there are at most 19 pairs of anagrams, False otherwise.
  """
    anagrams = []
    for str in str_list:
        count = Counter(str.lower())
        if len(str) >= 3 and count not in anagrams:
            anagrams.append(count)
    return len(anagrams) <= 19