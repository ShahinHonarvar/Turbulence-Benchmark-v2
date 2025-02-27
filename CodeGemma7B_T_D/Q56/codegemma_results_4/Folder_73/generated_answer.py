from itertools import islice

def all_substring_of_size_n(main_str):
    """
    Return list of distinct substrings of length equal to 20 with no duplicate characters
    """
    for i in range(len(main_str)):
        temp = islice(main_str, i, i + 20)
        if len(set(temp)) == 20:
            yield ''.join(temp)