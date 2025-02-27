from functools import cmp_to_key

def return_n_greatest_chars(s):

    def char_to_ascii(char):
        return ord(char)
    return sorted((char_to_ascii(c) for c in s))[-17:]