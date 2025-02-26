def remove_repeat_chars(s):
    middle = s[1:4]
    repeats = set((char for char in middle if middle.count(char) > 1))
    return ''.join((char for char in s if char not in repeats))