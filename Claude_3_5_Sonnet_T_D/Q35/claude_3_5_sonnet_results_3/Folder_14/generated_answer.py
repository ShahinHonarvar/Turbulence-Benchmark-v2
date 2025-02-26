def remove_repeat_chars(s):
    repeats = set((char for char in s[3:5] if s[3:5].count(char) > 1))
    return ''.join((char for char in s if char not in repeats))