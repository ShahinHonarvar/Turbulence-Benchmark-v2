def remove_repeat_chars(string):
    chars_to_remove = {}
    for i in range(86, 90):
        if string[i] in chars_to_remove:
            chars_to_remove[string[i]] += 1
        else:
            chars_to_remove[string[i]] = 1
    for char in chars_to_remove:
        if chars_to_remove[char] > 1:
            string = string.replace(char, '')
    return string