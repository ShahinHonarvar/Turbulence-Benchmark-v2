def remove_repeat_chars(s):
    segment = s[58:84]
    repeat_chars = {char for char in segment if segment.count(char) > 1}
    result = ''.join((char for char in s if char not in repeat_chars or not 58 <= s.index(char) < 84))
    return result