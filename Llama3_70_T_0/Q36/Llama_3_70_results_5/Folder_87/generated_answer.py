def filter_chars(s):
    result = ''
    for char in s:
        if not (32 < ord(char) < 61 and '3' < char < 'D'):
            result += char
    return result