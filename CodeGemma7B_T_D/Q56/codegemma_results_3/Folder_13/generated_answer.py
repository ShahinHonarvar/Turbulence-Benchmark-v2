from itertools import combinations_with_replacement
from collections import Counter

def all_substring_of_size_n(string):
    longest_length = 53
    if len(string) < longest_length:
        return []
    substring_list = []
    for x in combinations_with_replacement(string, longest_length):
        substring = ''.join(x)
        if len(set(substring)) == longest_length:
            substring_list.append(substring)
    return substring_list