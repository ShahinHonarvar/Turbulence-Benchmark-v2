def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if i < 42 or i >= 67 or char <= '6' or (char >= 'g'):
            result.append(char)
    return ''.join(result)