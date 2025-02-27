def remove_repeat_chars(s):
    seen_chars = set()
    new_string = ''
    for i, char in enumerate(s):
        if 40 < i < 200:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        new_string += char
    return new_string