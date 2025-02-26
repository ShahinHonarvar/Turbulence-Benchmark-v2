def filter_chars(string):
    result = list(string)
    for i in range(36, 41):
        if i < len(string):
            char = string[i]
            if 'H' <= char <= 'e':
                result = [c for c in result if c != char]
    return ''.join(result)