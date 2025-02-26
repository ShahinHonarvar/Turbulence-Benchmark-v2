def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 603 <= i <= 759 and 'Q' <= char <= 'h':
            result.extend((c for c in s if c != char))
            return ''.join(result)
    return s