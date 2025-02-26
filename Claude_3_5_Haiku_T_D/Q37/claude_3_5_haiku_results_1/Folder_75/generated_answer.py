def filter_chars(string):
    result = list(string)
    for i in range(34, 68):
        if i < len(string):
            char = string[i]
            if 'W' <= char <= 'x':
                result = [c for c in result if c != char]
    return ''.join(result)