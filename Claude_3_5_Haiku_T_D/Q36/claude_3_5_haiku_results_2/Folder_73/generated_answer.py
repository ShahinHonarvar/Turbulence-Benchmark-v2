def filter_chars(s):
    result = list(s)
    for i in range(67, 90):
        char = chr(i)
        if char > '#' and char < 'T':
            result = [c for c in result if c != char]
    return ''.join(result)