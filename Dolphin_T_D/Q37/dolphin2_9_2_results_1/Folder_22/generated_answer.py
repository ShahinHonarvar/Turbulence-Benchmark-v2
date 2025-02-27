def filter_chars(s):
    result = []
    for c in s:
        if ord(c) >= ord('7') and ord(c) <= ord('k') and (33 <= s.index(c) <= 70):
            continue
        result.append(c)
    return ''.join(result)