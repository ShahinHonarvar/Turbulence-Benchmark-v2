def remove_repeat_chars(s):
    target_substr = s[1:6]
    chars_to_remove = set((char for char in target_substr if target_substr.count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))