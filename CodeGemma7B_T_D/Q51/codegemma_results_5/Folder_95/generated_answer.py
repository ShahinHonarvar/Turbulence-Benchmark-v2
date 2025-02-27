def if_contains_anagrams(str_list):
    """
    Checks if a list of strings contains at most 6 pairs of anagrams.

    Args:
        str_list: A list of strings.

    Returns:
        True if there are at most 6 pairs of anagrams in the given list, False otherwise.
    """
    anagrams = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    anagrams_of_length_three_or_more = []
    for anagram, strings in anagrams.items():
        if len(anagram) >= 3:
            anagrams_of_length_three_or_more.append(anagram)
    if len(anagrams_of_length_three_or_more) <= 6:
        return True
    else:
        return False