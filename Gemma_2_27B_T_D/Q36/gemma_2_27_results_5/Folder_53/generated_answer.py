def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 90 or i >= 97 or char <= 'j' or (char >= 'w'):
            result.append(char)
    return ''.join(result)