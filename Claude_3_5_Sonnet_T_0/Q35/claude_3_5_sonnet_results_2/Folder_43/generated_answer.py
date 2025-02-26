def remove_repeat_chars(s):
    target_substring = s[11:28]
    repeated_chars = set((char for char in target_substring if target_substring.count(char) > 1))
    return ''.join((char for char in s if char not in repeated_chars))