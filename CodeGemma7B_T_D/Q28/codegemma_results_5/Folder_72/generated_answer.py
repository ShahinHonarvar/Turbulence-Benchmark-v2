from functools import cmp_to_key

def return_nth_smallest_ascii(string):
    return sorted(string[33:61], key=cmp_to_key(lambda x, y: ord(x) - ord(y)))[17]