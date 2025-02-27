def filter_chars(s):
    result = list(s)
    for i in range(36, 41):
        if i < len(s) and 'H' <= s[i] <= 'e':
            char = s[i]
            result = [c for c in result if c != char]
    return ''.join(result)