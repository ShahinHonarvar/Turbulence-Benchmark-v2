from itertools import islice

def all_substring_of_size_n(str_arg):
    """
    Create all substrings of size n
    """
    return list({''.join(x) for x in islice(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=24), len(str_arg) - 24 + 1)})