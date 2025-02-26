def filter_chars(string):
    result = list(string)
    for i in range(43, 78):
        char = string[i]
        if '!' < char < '?':
            result = [c for c in result if c != char]
    return ''.join(result)