def filter_chars(s):
    result = list(s)
    for i in range(62, 88):
        if '%' < s[i] < 'q':
            char_to_remove = s[i]
            result = [char for char in result if char != char_to_remove]
    return ''.join(result)