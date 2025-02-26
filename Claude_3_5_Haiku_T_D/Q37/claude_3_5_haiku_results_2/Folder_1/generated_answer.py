def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 41 <= i <= 79 and 'f' <= char <= '|':
            result.append((c for c in s if c != char))
            return ''.join(result[0])
    return s