from functools import cmp_to_key

def return_n_greatest_chars(s):
    characters = list(s)
    characters.sort(key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=True)
    return characters[:61]