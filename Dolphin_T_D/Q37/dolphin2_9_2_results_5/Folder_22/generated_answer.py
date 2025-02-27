def filter_chars(s):
    result = ''
    for char in s:
        if not (ord(char) >= ord('7') and ord(char) <= ord('k') and (33 <= s.index(char) <= 70)):
            result += char
    return result