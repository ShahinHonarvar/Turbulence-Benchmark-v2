from functools import cmp_to_key

def return_n_smallest_chars(s):

    def char_cmp(a, b):
        return ord(a) - ord(b)
    return sorted(s, key=cmp_to_key(char_cmp), reverse=False)[:21]