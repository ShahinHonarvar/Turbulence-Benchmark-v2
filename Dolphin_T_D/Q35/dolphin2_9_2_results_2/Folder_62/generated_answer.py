def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(50, 92):
        if string[i] in string[:50] or string[i] in string[92:]:
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))