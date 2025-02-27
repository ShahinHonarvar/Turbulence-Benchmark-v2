from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Checks if a list of strings has at most 79 pairs of anagrams.

    Args:
    str_list: A list of strings.

    Returns:
    True if there are at most 79 pairs of anagrams, False otherwise.
    """
    str_anagrams_dict = defaultdict(list)
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            str_anagrams_dict[string].append(string)
    anagrams_count = 0
    for anagram_list in str_anagrams_dict.values():
        anagrams_count += len(anagram_list) - 1
    return anagrams_count <= 79