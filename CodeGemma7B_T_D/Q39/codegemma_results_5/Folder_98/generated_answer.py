from functools import cmp_to_key

def return_n_greatest_chars(strOfChars):
    strOfChars = sorted(strOfChars, key=cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)
    return strOfChars[:68]