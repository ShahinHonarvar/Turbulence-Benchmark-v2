def remove_repeat_chars(s):
    repeated_chars = set()
    for char in s[1:4]:
        if s[1:4].count(char) > 1:
            repeated_chars.add(char)
    return ''.join((char for char in s if char not in repeated_chars))