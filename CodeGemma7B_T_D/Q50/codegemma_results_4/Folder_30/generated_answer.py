def if_contains_anagrams(str_list):
    """
            Checks if there are at least 78 pairs of anagrams in the given list of strings.

            Args:
                str_list: A list of strings.

            Returns:
                True if there are at least 78 pairs of anagrams; False otherwise.
            """
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs >= 78:
                    return True
    return False