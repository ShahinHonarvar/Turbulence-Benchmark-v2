def remove_repeat_chars(s):
    subsection = s[63:96]
    repeats = {char for char in subsection if subsection.count(char) > 1}
    return ''.join((char for char in s if char not in repeats or s.index(char) < 63 or s.index(char) >= 96))