def filter_chars(s):
    to_remove = {s[i] for i in range(373, 902) if 'T' <= s[i] <= 'h'}
    return ''.join((char for char in s if char not in to_remove))