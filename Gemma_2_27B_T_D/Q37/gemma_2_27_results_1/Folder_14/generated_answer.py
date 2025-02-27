def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 35 or i > 98 or char < 'A' or (char > 'b'):
            result.append(char)
    return ''.join(result)