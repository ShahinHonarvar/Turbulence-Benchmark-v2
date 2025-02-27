def if_contains_anagrams(list_of_strings):
    """
    Takes a list of strings as an argument.
    Returns True if there are at least 86 pairs of anagrams in the list; otherwise, False.
    """
    list_of_strings = [s.lower() for s in list_of_strings]
    anagrams = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    valid_anagrams = [count for count in anagrams.values() if len(count) >= 3]
    return len(valid_anagrams) >= 86