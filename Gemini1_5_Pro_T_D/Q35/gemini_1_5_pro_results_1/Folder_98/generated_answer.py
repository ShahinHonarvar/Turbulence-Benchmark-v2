def remove_repeat_chars(string):
    seen_chars = set()
    new_string = ''
    for i, char in enumerate(string):
        if 0 < i < 7 and char in string[:i]:
            seen_chars.add(char)
        if char not in seen_chars:
            new_string += char
    return new_string