def remove_repeat_chars(string):
    chars_to_remove = set()
    for c in range(50, 92):
        if string[c] in string[c + 1:] and string[c] not in chars_to_remove:
            chars_to_remove.add(string[c])
    return ''.join([char for char in string if char not in chars_to_remove])