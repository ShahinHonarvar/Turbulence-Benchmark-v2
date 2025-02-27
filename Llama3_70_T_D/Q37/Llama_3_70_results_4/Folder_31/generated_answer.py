def filter_chars(s):
    result = ''
    for char in s:
        if (ord(char) < 57 or ord(char) > 96) or (ord(char) < ord('<') or ord(char) > ord('w')):
            result += char
    return result