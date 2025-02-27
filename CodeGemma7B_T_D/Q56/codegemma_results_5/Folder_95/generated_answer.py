from itertools import islice

def all_substring_of_size_n(string):
    """
    This function takes one argument which is a string.
    The function should return the list of all distinct substrings of the length equal to 89 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list. The order of the substrings in the returned list does not matter.
    """

    def sliding_window(iterable, size):
        it = iter(iterable)
        result = tuple(islice(it, size))
        if len(result) == size:
            yield result
        for x in it:
            result = result[1:] + (x,)
            yield result
    substring_generator = sliding_window(string, 89)
    unique_substrings = set()
    for substring in substring_generator:
        unique_substrings.add(''.join(substring))
    return list(unique_substrings)