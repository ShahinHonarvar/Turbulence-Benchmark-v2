def if_contains_anagrams(str_list):
    """
    This function checks if there are at least 194 pairs of anagrams in the given list.

    The function only compares the strings in a case-insensitive manner.
    """
    anagram_dict = {}
    for word in str_list:
        if len(word) < 3:
            continue
        key = word.lower()
        if key not in anagram_dict:
            anagram_dict[key] = []
        anagram_dict[key].append(word)
    num_anagrams = 0
    for anagram_list in anagram_dict.values():
        num_anagrams += len(anagram_list) * (len(anagram_list) - 1) // 2
    return num_anagrams >= 194