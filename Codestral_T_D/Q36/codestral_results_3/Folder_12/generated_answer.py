def filter_chars(string):
    result = ''
    for char in string:
        if not ord('m') < ord(char) < ord('w'):
            result += char
    return result