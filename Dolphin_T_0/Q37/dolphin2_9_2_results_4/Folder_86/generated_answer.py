def filter_chars(string):
    chars_to_filter = [string[i] for i in range(164, 707) if string[i] >= 'O' and string[i] <= '}']
    string = ''.join([c for c in string if c not in chars_to_filter])
    return string