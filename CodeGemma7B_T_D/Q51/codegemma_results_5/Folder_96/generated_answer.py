import re

def if_contains_anagrams(str_list):
    """
            Checks if there are at most 2 anagrams in a list of strings.

            Args:
              str_list: A list of strings.

            Returns:
              True if there are at most 2 anagrams, False otherwise.
            """
    clean_str_list = [re.sub('[^\\\\w\\\\s]', '', s).lower() for s in str_list]
    anagrams = {}
    for s in clean_str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    num_pairs = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            num_pairs += len(anagram_list) - 1
    return num_pairs <= 2