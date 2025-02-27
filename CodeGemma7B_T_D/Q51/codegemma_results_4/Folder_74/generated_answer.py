def if_contains_anagrams(str_list):
    """
            Checks if there are at most 57 pairs of anagrams in the given list.

            Args:
                str_list: A list of strings.

            Returns:
                True if there are at most 57 pairs of anagrams, False otherwise.
            """
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    anagrams = {}
    for s in str_list:
        sorted_s = ''.join(sorted([c for c in s if c.isalnum()]))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = 1
        else:
            anagrams[sorted_s] += 1
            if anagrams[sorted_s] > 57:
                return False
    return True