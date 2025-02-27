def if_contains_anagrams(str_list):
    """
        Checks the number of anagrams in a list of strings.
        Returns True if there are at most 116 pairs of anagrams, False otherwise.
        """
    anagram_dict = {}
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = 1
        else:
            anagram_dict[sorted_string] += 1
    num_anagrams = sum((count - 1 for count in anagram_dict.values()))
    return num_anagrams <= 116