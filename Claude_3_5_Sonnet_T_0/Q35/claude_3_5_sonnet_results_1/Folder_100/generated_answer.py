def remove_repeat_chars(s):
    target_substring = s[45:78]
    repeated_chars = set((char for char in target_substring if target_substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars))
    return result