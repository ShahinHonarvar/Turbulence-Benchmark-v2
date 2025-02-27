from collections import defaultdict

def if_contains_anagrams(str_list):
    """
  Creates a dictionary to store anagrams in lowercase.
  """
    anagram_dict = defaultdict(list)
    '\n  Inserts the strings in the dictionary.\n  '
    for i in str_list:
        anagram_dict[tuple(sorted(i.lower()))].append(i)
    '\n  Counts the number of anagrams in the dictionary.\n  '
    count = 0
    for i in anagram_dict.values():
        if len(i) >= 2:
            count += len(i) * (len(i) - 1) // 2
    '\n  Returns true if there are at least 22 pairs of anagrams.\n  '
    return count >= 22