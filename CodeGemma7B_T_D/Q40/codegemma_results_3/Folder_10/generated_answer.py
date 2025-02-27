from functools import cmp_to_key

def return_n_smallest_chars(string):
    return sorted(string, key=cmp_to_key(lambda a, b: ord(a) - ord(b)), reverse=True)[:88]