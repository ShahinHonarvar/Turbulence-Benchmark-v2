def filter_chars(s):
    result = ''
    for char in s:
        if (ord(char) < 90 or ord(char) > 97) or not 'j' < char < 'w':
            result += char
    return result