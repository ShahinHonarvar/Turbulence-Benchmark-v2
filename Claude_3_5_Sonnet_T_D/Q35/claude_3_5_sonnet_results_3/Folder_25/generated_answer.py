def remove_repeat_chars(s):
    if len(s) <= 38:
        return s
    segment = s[37:43]
    chars_to_remove = set([char for char in segment if segment.count(char) > 1])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result