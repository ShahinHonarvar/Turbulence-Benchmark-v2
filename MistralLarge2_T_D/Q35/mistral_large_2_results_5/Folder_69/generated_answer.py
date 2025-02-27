def remove_repeat_chars(s):
    substring = s[39:43]
    repeated_chars = {char for char in substring if substring.count(char) > 1}
    result = ''.join([char for char in s if char not in repeated_chars])
    return result