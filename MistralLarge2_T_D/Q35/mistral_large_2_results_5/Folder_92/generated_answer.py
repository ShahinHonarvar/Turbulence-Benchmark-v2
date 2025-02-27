def remove_repeat_chars(s):
    unique_chars = set(s[1:3])
    repeated_chars = {char for char in unique_chars if s[1:3].count(char) > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result