def filter_chars(s):
    result = list(s)
    for i in range(343, 665):
        if '%' < s[i] < 'U':
            char_to_remove = s[i]
            result = [c for c in result if c != char_to_remove]
    return ''.join(result)