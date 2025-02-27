from functools import cmp_to_key

def return_n_greatest_chars(word):
    return sorted(word, key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=False)[:32]