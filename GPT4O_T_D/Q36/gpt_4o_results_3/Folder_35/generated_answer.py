def filter_chars(s):
    exclude_chars = set()
    for char in s[164:658]:
        if '(' < char < ']':
            exclude_chars.add(char)
    return ''.join((char for char in s if char not in exclude_chars))