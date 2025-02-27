def filter_chars(s):
    result = ''
    for char in s:
        if ord(char) > ord('I') and ord(char) < ord('a') and (49 <= ord(char) <= 56):
            continue
        else:
            result += char
    return result