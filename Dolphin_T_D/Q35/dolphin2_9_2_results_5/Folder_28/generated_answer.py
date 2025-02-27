def remove_repeat_chars(string):
    chars_to_remove = {char: string.count(char) for char in string}
    for i in range(86, 100, 1):
        char = string[i]
        if chars_to_remove[char] > 1:
            string = string.replace(char, '')
    return string