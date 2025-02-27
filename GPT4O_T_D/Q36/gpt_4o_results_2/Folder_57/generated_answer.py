def filter_chars(s):
    filtered_chars = set()
    if len(s) > 74:
        for char in s[71:74]:
            if 'A' < char < 'U':
                filtered_chars.add(char)
    return ''.join((c for c in s if c not in filtered_chars))