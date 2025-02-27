def remove_repeat_chars(s):
    segment = s[44:67]
    to_remove = {char for char in segment if segment.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))