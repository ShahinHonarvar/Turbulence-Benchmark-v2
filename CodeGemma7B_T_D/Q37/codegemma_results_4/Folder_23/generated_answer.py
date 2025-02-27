def filter_chars(string):
    return ''.join((c for c in string if (c < 'V' or c > 'Y') or (c <= string[50] or c >= string[78])))