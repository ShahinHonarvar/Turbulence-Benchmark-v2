from itertools import combinations

def all_substring_of_size_n(text):
    """
    This function takes one argument which is a string.
    The function returns the list of all distinct substrings of the length equal to 14 with no duplicate characters.
    If no such substrings exist in the given string, the function returns an empty list.
    """
    if len(text) < 14:
        return []
    else:
        result = []
        for c in combinations(text, 14):
            if len(set(c)) == 14:
                result.append(''.join(c))
        return result