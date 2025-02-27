def remove_repeat_chars(s):
    segment = s[45:91]
    repeat_chars = {char for char in segment if segment.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 44 or s.index(char) >= 91))