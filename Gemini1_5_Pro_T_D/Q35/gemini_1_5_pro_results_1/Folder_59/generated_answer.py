def remove_repeat_chars(string):
    seen_chars = set()
    new_string = ''
    for i, char in enumerate(string):
        if 0 < i < 10:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        new_string += char
    return new_string