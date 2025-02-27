def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (23 <= i <= 89 and 'w' <= char <= '{'):
            result.append(char)
    return ''.join(result)