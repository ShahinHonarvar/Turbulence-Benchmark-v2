from functools import cmp_to_key

def return_n_greatest_chars(n):
    return sorted(n, key=cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)[:55]