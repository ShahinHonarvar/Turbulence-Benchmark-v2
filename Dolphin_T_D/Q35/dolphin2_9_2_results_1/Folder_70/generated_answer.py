def remove_repeat_chars(string):
    chars = {}
    for char in string[43:70]:
        if char in chars:
            string = string.replace(char, '')
        else:
            chars[char] = 1
    return string