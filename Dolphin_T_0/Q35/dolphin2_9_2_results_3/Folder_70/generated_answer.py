def remove_repeat_chars(string):
    char_dict = {}
    result = ''
    for i, char in enumerate(string):
        if 43 < i < 70:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    for char in string:
        if char not in char_dict:
            result += char
    return result