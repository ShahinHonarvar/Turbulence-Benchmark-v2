from functools import cmp_to_key

def return_n_smallest_chars(str):
    """
    Returns a list of the n smallest characters in a string.
    """

    def compare_chars(char1, char2):
        """
        Compares two characters by their ASCII values.
        """
        return ord(char1) - ord(char2)
    sorted_str = sorted(str, key=cmp_to_key(compare_chars))
    return sorted_str[:87]