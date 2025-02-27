def if_contains_anagrams(str_lst):
    """This function checks if there are at most 26 pairs of anagrams in a list of strings.

    The function only considers anagrams of the English letters, and it only considers anagrams of the length of at least three.

    The function compares the strings in a case-insensitive manner."""
    anagrams = {}
    for s in str_lst:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for count in anagrams.values():
        if count > 26:
            return False
    return True