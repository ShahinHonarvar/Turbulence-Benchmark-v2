def if_contains_anagrams(str_list):
    """
  This function checks if there are at most 407 pairs of anagrams in the given list.
  """
    anagram_pairs = set()
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower().replace(' ', '')
            str2 = str_list[j].lower().replace(' ', '')
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                anagram_pairs.add((str1, str2))
    return len(anagram_pairs) <= 407