def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = ''
    for char in s:
        if char_count[char] == 1 or ord(char) < 27 or ord(char) > 96:
            result += char
    return result