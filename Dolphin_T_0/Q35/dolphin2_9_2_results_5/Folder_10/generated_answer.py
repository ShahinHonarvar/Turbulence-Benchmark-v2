def remove_repeat_chars(s):
    count = {}
    result = ''
    for i in range(36, 54):
        char = s[i]
        if char not in count:
            count[char] = 1
            result += char
        elif count[char] == 1:
            result += char
        else:
            result += ' '
    return result