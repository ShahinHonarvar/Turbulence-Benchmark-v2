from functools import cmp_to_key
from operator import itemgetter

def return_n_greatest_chars(string):
    char_ascii_tuples = [(char, ord(char)) for char in string]
    sorted_tuples = sorted(char_ascii_tuples, key=itemgetter(1), reverse=True)
    n_greatest_chars = [char for char, _ in sorted_tuples[:72]]
    return n_greatest_chars