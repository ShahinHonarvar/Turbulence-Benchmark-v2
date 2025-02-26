def remove_repeat_chars(s):
    if len(s) <= 5:
        return s
    substring = s[3:5]
    chars_to_remove = set()
    for char in substring:
        if substring.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))