def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    substr = s[1:8]
    repeat_chars = set()
    for char in substr:
        if substr.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars))
    return result