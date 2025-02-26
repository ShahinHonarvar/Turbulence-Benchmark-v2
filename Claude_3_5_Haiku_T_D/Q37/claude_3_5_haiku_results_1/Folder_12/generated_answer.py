def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 19 <= i <= 90 and 'F' <= char <= 'h':
            result.extend((c for c in s if c != char))
            break
    return ''.join(result) if result else s