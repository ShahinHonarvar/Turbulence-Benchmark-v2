def remove_repeat_chars(string):
    char_count = {}
    for i in range(16, 87):
        char = string[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = ''
    for char in string:
        if char_count.get(char, 0) <= 1:
            result += char
    return result