def remove_repeat_chars(s):
    chars_to_remove = []
    for char in s[1:5]:
        if s[1:5].count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.append(char)
    return ''.join([char for char in s if char not in chars_to_remove])