def remove_repeat_chars(s):
    substring = s[86:89]
    substring_chars = set(substring)
    result = [char for char in s if char not in substring_chars or substring.count(char) == 1]
    return ''.join(result)