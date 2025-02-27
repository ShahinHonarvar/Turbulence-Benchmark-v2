def filter_chars(s):
    filtered = set()
    if len(s) > 70:
        for char in s[33:71]:
            if '7' <= char <= 'k':
                filtered.add(char)
    return ''.join((char for char in s if char not in filtered))