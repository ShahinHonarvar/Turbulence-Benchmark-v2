def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    subset = s[44:70]
    repeat_chars = {char for char in subset if subset.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))