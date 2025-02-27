from functools import cmp_to_key

def return_n_smallest_chars(string):
    ascii_values = {ord(char): char for char in string}
    sorted_chars = sorted(ascii_values.values(), key=cmp_to_key(lambda x, y: ord(x) - ord(y)))
    return sorted_chars[:66]