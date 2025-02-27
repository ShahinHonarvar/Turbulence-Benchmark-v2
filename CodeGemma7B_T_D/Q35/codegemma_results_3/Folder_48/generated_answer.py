def remove_repeat_chars(string):
    seen = set()
    new_string = ''
    for i, char in enumerate(string):
        if i < 409 or i >= 502 or char in seen:
            continue
        seen.add(char)
        new_string += char
    return new_string