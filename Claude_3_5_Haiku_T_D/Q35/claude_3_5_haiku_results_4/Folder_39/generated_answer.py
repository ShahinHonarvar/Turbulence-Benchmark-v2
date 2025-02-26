def remove_repeat_chars(s):
    if len(s) <= 45:
        return s
    substr = s[45:91]
    chars_to_remove = set()
    for char in substr:
        if substr.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.add(char)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result