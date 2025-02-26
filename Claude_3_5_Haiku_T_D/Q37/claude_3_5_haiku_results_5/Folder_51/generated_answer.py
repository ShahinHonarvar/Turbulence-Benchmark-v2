def filter_chars(s):
    result = list(s)
    for i in range(36, 41):
        if 0 <= i < len(s):
            char = s[i]
            if 'H' <= char <= 'e':
                result = [c for c in result if c != char]
    return ''.join(result)