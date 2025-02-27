def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    segment = s[38:43]
    repeat_chars = {char for char in segment if segment.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))