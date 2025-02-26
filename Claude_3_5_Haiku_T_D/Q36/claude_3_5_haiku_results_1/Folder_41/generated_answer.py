def filter_chars(s):
    result = list(s)
    for i in range(82, 89):
        if 'f' < s[i] < '{':
            char = s[i]
            result = [c for c in result if c != char]
    return ''.join(result)