def remove_repeat_chars(string):
    chars = set()
    result = ''
    for char in string:
        if char not in chars:
            chars.add(char)
            result += char
        elif 34 < string.index(char) < 69:
            result = result.replace(char, '')
    return result