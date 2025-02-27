def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    middle_substring = s[1:4]
    chars_to_remove = {char for char in middle_substring if middle_substring.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))