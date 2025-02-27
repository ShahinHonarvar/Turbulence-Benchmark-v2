def remove_repeat_chars(string):
    char_count = {}
    for char in string[57:85]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    for repeat_char in repeat_chars:
        string = string.replace(repeat_char, '')
    return string