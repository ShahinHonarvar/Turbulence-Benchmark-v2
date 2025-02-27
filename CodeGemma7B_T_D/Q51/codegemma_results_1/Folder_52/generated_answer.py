import itertools

def if_contains_anagrams(str_list):
    """This function checks if a list of words contains anagrams.
            Args:
                str_list: The list of words.
            Returns:
                True if there are at most 43 pairs of anagrams in the list, False otherwise.
            """
    pairs = itertools.combinations(str_list, 2)
    anagrams = [(s1, s2) for s1, s2 in pairs if is_anagram(s1, s2) and len(s1) >= 3 and (len(s2) >= 3)]
    return len(anagrams) <= 43