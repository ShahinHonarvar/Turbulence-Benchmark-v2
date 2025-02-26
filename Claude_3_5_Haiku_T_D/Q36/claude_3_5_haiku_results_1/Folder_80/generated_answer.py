def filter_chars(s):
    result = list(s)
    for i in range(55, 92):
        char = s[i]
        if 'J' < char < 'X':
            result = [x for x in result if x != char]
    return ''.join(result)