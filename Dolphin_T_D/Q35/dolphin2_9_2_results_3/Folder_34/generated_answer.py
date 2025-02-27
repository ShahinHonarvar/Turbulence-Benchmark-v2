def remove_repeat_chars(string):
    char_dict = {}
    result = ''
    for char in string:
        if 70 <= ord(char) <= 200:
            if char_dict.get(char):
                continue
            else:
                char_dict[char] = 1
                result += char
        else:
            result += char
    return result