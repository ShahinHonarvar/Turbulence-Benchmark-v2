def remove_repeat_chars(string):
    chars = {}
    for i in range(17, 88):
        char = string[i]
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    result = ''
    for char in string:
        if chars.get(char, 0) <= 1:
            result += char
    return result