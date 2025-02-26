def filter_chars(string):
    result = list(string)
    for i in range(163, 658):
        if '(' < result[i] < ']':
            char_to_remove = result[i]
            result = [c for c in result if c != char_to_remove]
    return ''.join(result)