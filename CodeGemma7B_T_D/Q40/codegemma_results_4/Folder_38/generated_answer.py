from functools import cmp_to_key

def return_n_smallest_chars(string):
    list = sorted(list(string), key=cmp_to_key(lambda char1, char2: ord(char1) - ord(char2)))
    return list[:45]