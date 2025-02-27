def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (36 <= i <= 40 and 'H' <= char <= 'e'):
            result.append(char)
    return ''.join(result)