def if_contains_anagrams(str_list):
    """
            Checks if there are at most 73 pairs of anagrams in the given list.

            Args:
                str_list: A list of strings.

            Returns:
                True if there are at most 73 pairs of anagrams, False otherwise.
            """
    str_list.sort(key=len)
    anagrams = {}
    for word in str_list:
        sorted_letters = ''.join(sorted(word.lower()))
        if sorted_letters in anagrams:
            anagrams[sorted_letters] += 1
            if anagrams[sorted_letters] > 73:
                return True
        else:
            anagrams[sorted_letters] = 1
    return False