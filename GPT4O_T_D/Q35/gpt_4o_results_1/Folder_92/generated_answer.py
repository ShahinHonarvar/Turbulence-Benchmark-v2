def remove_repeat_chars(s):
    chars_to_remove = set()
    if 0 < len(s) - 1:
        for char in s[1:2]:
            if s[1:2].count(char) > 1:
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))