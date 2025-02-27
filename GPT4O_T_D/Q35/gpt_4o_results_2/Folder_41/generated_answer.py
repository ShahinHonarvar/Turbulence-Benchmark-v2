def remove_repeat_chars(s):
    substring = s[4:8]
    to_remove = {char for char in substring if substring.count(char) > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result