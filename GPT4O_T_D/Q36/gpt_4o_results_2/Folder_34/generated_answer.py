def filter_chars(s):
    filtered_chars = set()
    for char in s[11:79]:
        if '?' < char < 'm':
            filtered_chars.add(char)
    return ''.join((char for char in s if char not in filtered_chars))