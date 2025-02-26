def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 24 <= i <= 79 and 'a' <= char <= 'f':
            result.extend((c for c in s if c != char))
            break
        result.append(char)
    return ''.join(result + s[len(result):])