from functools import cmp_to_key

def return_nth_smallest_ascii(string):
    return sorted(string, key=cmp_to_key(lambda c1, c2: ord(c1) - ord(c2)))[8]