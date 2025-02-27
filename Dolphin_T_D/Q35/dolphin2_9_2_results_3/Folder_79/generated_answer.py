def remove_repeat_chars(string):
    uniq_chars = set(string)
    for char in uniq_chars:
        if string.count(char) > 1 and 1 < string.index(char) < 7:
            string = string.replace(char, '')
    return string