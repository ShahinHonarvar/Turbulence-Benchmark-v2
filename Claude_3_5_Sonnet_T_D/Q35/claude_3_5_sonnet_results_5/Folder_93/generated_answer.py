def remove_repeat_chars(s):
    if len(s) <= 58:
        return s
    start = 58
    end = min(85, len(s))
    substring = s[start:end]
    chars_to_remove = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result