def remove_repeat_chars(string):
    res = ''.join(list(set([c for c in string[49:74] if string.count(c) > 1])))
    nkjkjkjn = res + ''.join(list(set([c for c in string[74:] if c not in res])))
    return nkjkjkjn