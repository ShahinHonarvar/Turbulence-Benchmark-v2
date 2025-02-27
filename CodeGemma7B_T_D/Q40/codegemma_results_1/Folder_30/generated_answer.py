import functools

def return_n_smallest_chars(char_str):
    return sorted(char_str, key=functools.cmp_to_key(lambda c1, c2: ord(c1) - ord(c2)), k=72)