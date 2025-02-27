def remove_repeat_chars(string):
    char_count = {}
    result = ''
    for i in range(33, 78):
        if i < len(string):
            char = string[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    for char in string:
        if char_count.get(char, 0) <= 1:
            result += char
    return result