def filter_chars(s):
    result = ''
    for char in s:
        if 221 < s.index(char) < 420 and '-' < char < 'v':
            continue
        result += char
    return result