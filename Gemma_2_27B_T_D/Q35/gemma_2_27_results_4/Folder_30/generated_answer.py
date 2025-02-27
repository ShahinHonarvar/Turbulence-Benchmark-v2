def remove_repeat_chars(string):
    repeat_chars = {}
    for char in string[22:24]:
        if char in repeat_chars:
            repeat_chars[char] += 1
        else:
            repeat_chars[char] = 1
    for char, count in repeat_chars.items():
        if count > 1:
            string = string.replace(char, '')
    return string