def remove_repeat_chars(s):
    substring = s[4:9]
    to_remove = set((char for char in substring if substring.count(char) > 1))
    return ''.join((char for char in s if char not in to_remove))