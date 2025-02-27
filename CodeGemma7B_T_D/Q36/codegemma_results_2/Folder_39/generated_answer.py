def filter_chars(s):
    result = []
    for i in range(43, 59):
        char = s[i]
        if char > '5' and char < 'C':
            result = [c for c in result if c != char]
        else:
            result.append(char)
    return ''.join(result)