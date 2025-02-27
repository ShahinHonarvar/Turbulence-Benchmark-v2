def remove_repeat_chars(string):
    chars = {}
    for i in range(30, 200):
        if i < len(string):
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