from itertools import combinations

def all_substring_of_size_n(text, n=130):
    """
            This function takes one argument which is a string. The function should return the list of all distinct substrings of the length equal to 130 with no duplicate characters. If no such substrings exist in the given string, the function should return an empty list. The order of the substrings in the returned list does not matter.
            """

    def remove_duplicates(text):
        """
                This function removes duplicates from a given string.
                """
        return ''.join(set(text))

    def get_distinct_substrings(text, n):
        """
                This function returns the list of all distinct substrings of the length equal to n with no duplicate characters in the given string.
                """
        substrings = []
        for i in range(len(text) + 1 - n):
            substring = text[i:i + n]
            substring = remove_duplicates(substring)
            if substring not in substrings:
                substrings.append(substring)
        return substrings
    substrings = get_distinct_substrings(text, n)
    if substrings:
        return substrings
    else:
        return []