from functools import cmp_to_key

def return_n_greatest_chars(string):

    def func(char_a, char_b):
        return ord(char_b) - ord(char_a)
    list_of_chars = list(string)
    list_of_chars.sort(key=cmp_to_key(func))
    return list_of_chars[:21]