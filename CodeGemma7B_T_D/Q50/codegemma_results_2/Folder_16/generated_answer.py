from collections import defaultdict
        from itertools import combinations

def if_contains_anagrams(str_list):
    """
            Checks if there are at least 155 pairs of anagrams in a list of strings.

            Args:
                str_list: A list of strings.

            Returns:
                True if there are at least 155 pairs of anagrams, False otherwise.
            """
    str_dict = defaultdict(list)
    for string in str_list:
        str_dict[''.join(sorted([c.lower() for c in string]))].append(string)
    anagram_count = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 3:
            anagram_count += len(list(combinations(anagram_list, 2)))
    return anagram_count >= 155