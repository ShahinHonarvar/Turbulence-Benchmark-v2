from functools import cmp_to_key

def return_n_greatest_chars(characters):
    if len(characters) < 76:
        return sorted(characters, key=cmp_to_key(lambda x, y: ord(y) - ord(x)))
    else:
        return sorted(characters[:76], key=cmp_to_key(lambda x, y: ord(y) - ord(x)))