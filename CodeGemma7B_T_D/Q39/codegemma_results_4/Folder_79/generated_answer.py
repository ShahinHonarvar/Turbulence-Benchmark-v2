from functools import cmp_to_key

def return_n_greatest_chars(chars):
    all_chars = list(chars)
    all_chars.sort(key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=True)
    return all_chars[:82]