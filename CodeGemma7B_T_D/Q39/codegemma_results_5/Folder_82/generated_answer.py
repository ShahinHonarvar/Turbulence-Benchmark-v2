from functools import cmp_to_key

def return_n_greatest_chars(string):
    return sorted(string, key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=False)[-60:]