def filter_chars(string):
    result = list(string)
    for i in range(66, 90):
        if i < len(string):
            char = string[i]
            if '#' < char < 'T':
                result = [c for c in result if c != char]
    return ''.join(result)