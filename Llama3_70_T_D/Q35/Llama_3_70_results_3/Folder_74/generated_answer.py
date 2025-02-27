def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = ''
    for char in s:
        if char_count[char] > 1 and ord(char) > 97 and (ord(char) < 69):
            continue
        else:
            result += char
    return result