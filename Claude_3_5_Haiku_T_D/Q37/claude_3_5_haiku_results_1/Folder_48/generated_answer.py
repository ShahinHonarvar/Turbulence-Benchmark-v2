def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 513 <= i <= 877 and '?' <= char <= 'n':
            result = [c for c in result if c != char]
        else:
            result.append(char)
    return ''.join(result)