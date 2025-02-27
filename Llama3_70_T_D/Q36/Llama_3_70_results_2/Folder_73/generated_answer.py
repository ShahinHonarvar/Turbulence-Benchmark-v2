def filter_chars(s):
    result = ''
    for char in s:
        if not (66 < ord(char) < 90 and char > '#' and (char < 'T')):
            result += char
    return result