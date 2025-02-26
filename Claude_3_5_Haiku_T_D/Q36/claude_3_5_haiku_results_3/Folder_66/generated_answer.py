def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 39 < i < 87 and '!' < char < '}':
            result.append(char not in s[:i])
        else:
            result.append(True)
    return ''.join((char for char, keep in zip(s, result) if keep))