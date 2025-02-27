def remove_repeat_chars(string):
    chars_to_remove = set(string[19:32])
    for c in chars_to_remove:
        if string[19:32].count(c) > 1:
            string = string.replace(c, '', string[19:32].index(c))
    return string