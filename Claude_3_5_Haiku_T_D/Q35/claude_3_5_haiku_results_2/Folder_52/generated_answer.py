def remove_repeat_chars(s):
    substring = s[39:81]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 39 or s.index(char) >= 81))
    return result