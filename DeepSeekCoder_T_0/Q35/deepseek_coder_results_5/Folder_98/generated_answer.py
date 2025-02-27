def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    middle_chars = s[1:7]
    repeat_chars = {char for char in middle_chars if middle_chars.count(char) > 1}
    result = s[0] + ''.join((char for char in s[1:-1] if char not in repeat_chars)) + s[-1]
    return result