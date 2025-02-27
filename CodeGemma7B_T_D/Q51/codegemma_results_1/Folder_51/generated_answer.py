from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Checks if a list of strings contains at most 116 pairs of anagrams.

    Args:
        str_list: A list of strings.

    Returns:
        True if there are at most 116 pairs of anagrams, False otherwise.
    """
    grouped_anagrams = defaultdict(list)
    for string in str_list:
        str_modified = string.replace(' ', '')
        str_modified = str_modified.lower()
        if len(str_modified) < 3:
            continue
        sorted_string = ''.join(sorted(str_modified))
        grouped_anagrams[sorted_string].append(string)
    num_pairs = 0
    for anagrams in grouped_anagrams.values():
        num_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return num_pairs <= 116