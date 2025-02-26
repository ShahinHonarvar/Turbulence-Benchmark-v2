def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 17 <= i <= 63 and 'O' <= char <= '^':
            result.append(''.join((c for c in s if c != char)))
            break
    return result[0] if result else s