def remove_repeat_chars(s):
    d = {chr(i): 0 for i in range(48, 77)}
    result = ''
    for char in s:
        if 48 <= ord(char) < 76 and d[char] == 1:
            continue
        if 48 <= ord(char) < 76:
            d[char] = 1
        result += char
    return result