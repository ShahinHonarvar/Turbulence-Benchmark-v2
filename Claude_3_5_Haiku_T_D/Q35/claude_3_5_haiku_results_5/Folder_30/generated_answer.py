def remove_repeat_chars(string):
    if len(string) <= 25:
        return string
    substr = string[23:24]
    chars_to_remove = set()
    for char in substr:
        if substr.count(char) > 1:
            chars_to_remove.add(char)
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result