def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(37, 43):
        if string[i] in string[i + 1:i + 43]:
            chars_to_remove.add(string[i])
    return ''.join([c for c in string if c not in chars_to_remove])