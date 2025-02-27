def remove_repeat_chars(s):
    temp_substring = s[39:52]
    repeated_chars = {char for char in temp_substring if temp_substring.count(char) > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result