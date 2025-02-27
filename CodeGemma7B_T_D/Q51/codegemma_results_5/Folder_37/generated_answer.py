from collections import defaultdict

def if_contains_anagrams(str_list):
    """
            Checks if there are at most 206 pairs of anagrams in a list of strings.

            Args:
            str_list: A list of strings.

            Returns:
            True if there are at most 206 pairs of anagrams, False otherwise.
            """
    anagrams = defaultdict(list)
    for string in str_list:
        anagrams[tuple(sorted(string.lower()))].append(string)
    return len(anagrams) <= 206