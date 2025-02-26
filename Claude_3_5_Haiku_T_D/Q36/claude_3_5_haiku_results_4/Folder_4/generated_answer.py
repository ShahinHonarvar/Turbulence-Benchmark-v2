def filter_chars(s):
    chars_to_remove = set(s[43:67][s[43:67] > '6'][s[43:67] < 'g'])
    return ''.join((char for char in s if char not in chars_to_remove))