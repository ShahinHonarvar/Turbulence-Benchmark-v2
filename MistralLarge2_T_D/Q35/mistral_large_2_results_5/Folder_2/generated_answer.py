def remove_repeat_chars(s):
    substr = s[72:93]
    to_remove = {char for char in substr if substr.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))