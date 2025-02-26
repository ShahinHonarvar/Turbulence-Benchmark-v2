def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 39 < i < 87 and '!' < char < '}':
            result.append(char)
    modified = s
    for char in result:
        modified = modified.replace(char, '')
    return modified