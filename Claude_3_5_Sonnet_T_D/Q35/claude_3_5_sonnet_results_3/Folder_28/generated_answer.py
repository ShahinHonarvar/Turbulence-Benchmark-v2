def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    start = 87
    end = min(99, len(s))
    substr = s[start:end]
    chars_to_remove = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result