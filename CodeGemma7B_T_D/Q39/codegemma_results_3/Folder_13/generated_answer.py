def return_n_greatest_chars(string):
    ascii = sorted([ord(x) for x in string], reverse=True)[0:31]
    return [chr(x) for x in ascii]