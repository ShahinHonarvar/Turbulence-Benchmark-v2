def filter_chars(s):
    result = []
    for ch in s:
        if 29 <= s.index(ch) <= 97 and '-' <= ch <= 'n':
            result.append(ch)
    return ''.join(sorted(set(result)))