def remove_repeat_chars(s):
    segment = s[26:80]
    repeated_chars = {char for char in segment if segment.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 25 or s.index(char) >= 80))