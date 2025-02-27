def filter_chars(s):
    result = ''
    for char in s:
        if ord('H') <= ord(char) <= ord('e') and 38 <= ord(char) <= 69:
            for c in result:
                if c != char:
                    result = result + c
        else:
            result += char
    return result