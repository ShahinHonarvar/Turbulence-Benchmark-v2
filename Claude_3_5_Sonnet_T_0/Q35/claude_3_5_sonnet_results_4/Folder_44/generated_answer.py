def remove_repeat_chars(s):
    target_substring = s[37:52]
    repeat_chars = set((char for char in target_substring if target_substring.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))