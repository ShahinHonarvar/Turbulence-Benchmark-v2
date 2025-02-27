def filter_chars(s):
    result = []
    for char in s:
        if char in string.ascii_uppercase and char > 'W' and (char < 'y'):
            continue
        result.append(char)
    return ''.join(result)