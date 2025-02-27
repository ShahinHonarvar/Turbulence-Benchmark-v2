def filter_chars(s):
    if len(s) <= 343:
        return s
    segment = s[344:665]
    to_remove = {char for char in segment if '%' < char < 'U'}
    result = ''.join((char for char in s if char not in to_remove or char not in s[344:665]))
    return result