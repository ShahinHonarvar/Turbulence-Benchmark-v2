def remove_repeat_chars(txt):
    chars_to_remove = set()
    for i in range(476, 710):
        char = txt[i]
        if txt.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join([char for char in txt if char not in chars_to_remove])