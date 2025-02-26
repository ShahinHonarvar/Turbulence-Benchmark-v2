def remove_repeat_chars(s):
    if len(s) <= 85:
        return s
    substr = s[78:84]
    chars_to_remove = set()
    for char in substr:
        if substr.count(char) > 1:
            chars_to_remove.add(char)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result