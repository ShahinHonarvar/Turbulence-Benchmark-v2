from functools import cmp_to_key

def return_nth_smallest_ascii(string):
    return sorted(string[16:66], key=cmp_to_key(lambda x, y: ord(x) - ord(y)))[7]