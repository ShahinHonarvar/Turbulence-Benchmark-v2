def remove_repeat_chars(s):
    if len(s) > 5:
        segment = s[3:5]
        remove_chars = {char for char in segment if segment.count(char) > 1}
        return ''.join((char for char in s if char not in remove_chars))
    return s