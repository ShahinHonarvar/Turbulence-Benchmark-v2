def remove_repeat_chars(string):
    char_count = {}
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char in char_count:
        if char_count[char] > 1 and string.index(char) >= 355 and (string.rindex(char) <= 988):
            string = string.replace(char, '')
    return string