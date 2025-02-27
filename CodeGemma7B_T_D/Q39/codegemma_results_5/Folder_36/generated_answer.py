from functools import cmp_to_key

def return_n_greatest_chars(str):
    result = sorted(str, key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=True)
    return result[:32]