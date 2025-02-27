def remove_repeat_chars(s):
    unique_chars = set()
    to_remove = set()
    for i, char in enumerate(s):
        if 33 < i < 78:
            if char in unique_chars:
                to_remove.add(char)
            else:
                unique_chars.add(char)
    result = ''.join((char for char in s if char not in to_remove))
    return result