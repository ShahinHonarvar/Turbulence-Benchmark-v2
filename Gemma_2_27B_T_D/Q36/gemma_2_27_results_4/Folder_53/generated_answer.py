def filter_chars(s):
    result = []
    for char in s:
        if 90 <= ord(char) < 97 or char <= 'j' or char >= 'w':
            result.append(char)
    return ''.join(result)