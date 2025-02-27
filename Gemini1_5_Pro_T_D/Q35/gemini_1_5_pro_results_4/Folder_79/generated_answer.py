def remove_repeat_chars(string):
    seen_chars = set()
    new_string = ''
    for i, char in enumerate(string):
        if 1 < i < 7 and string.count(char) > 1:
            if char not in seen_chars:
                seen_chars.add(char)
        else:
            new_string += char
    return new_string