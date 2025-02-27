def remove_repeat_chars(s):
    if not s or len(s) <= 98:
        return s
    substring = s[71:98]
    to_remove = {char for char in substring if substring.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove or not 71 < s.index(char) < 98))