def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    substr = s[38:43]
    chars_to_remove = set()
    for char in substr:
        if substr.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))