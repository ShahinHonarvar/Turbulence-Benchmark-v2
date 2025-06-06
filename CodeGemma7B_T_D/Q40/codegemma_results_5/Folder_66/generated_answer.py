from functools import cmp_to_key

def return_n_smallest_chars(string):
    return sorted(string, key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=True)[:33]