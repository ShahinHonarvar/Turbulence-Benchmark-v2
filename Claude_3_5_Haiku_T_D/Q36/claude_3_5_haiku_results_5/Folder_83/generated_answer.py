def filter_chars(string):
    result = list(string)
    for i in range(73, 93):
        if '<' < string[i] < 'J':
            char_to_remove = string[i]
            result = [c for c in result if c != char_to_remove]
    return ''.join(result)