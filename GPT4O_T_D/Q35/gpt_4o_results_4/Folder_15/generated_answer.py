def remove_repeat_chars(s):
    substr = s[1:4]
    chars_to_remove = {char for char in substr if substr.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))