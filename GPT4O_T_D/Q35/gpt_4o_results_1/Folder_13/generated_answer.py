def remove_repeat_chars(s):
    target_zone = s[47:91]
    repeated_chars = {char for char in target_zone if target_zone.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) < 47 or s.index(char) > 90))