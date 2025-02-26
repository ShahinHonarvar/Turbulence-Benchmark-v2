def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 38 <= i <= 69 and 'H' <= char <= 'e':
            result.append(char)
    filtered = ''.join(result)
    for char in filtered:
        s = s.replace(char, '')
    return s