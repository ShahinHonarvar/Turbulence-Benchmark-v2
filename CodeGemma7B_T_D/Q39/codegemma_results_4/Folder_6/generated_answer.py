from functools import cmp_to_key

def return_n_greatest_chars(given_string):
    return sorted(given_string, key=cmp_to_key(lambda x, y: y.encode().isalpha() and x.lower().encode().isalpha() and ord(y) - ord(x)))[:47]