def remove_repeat_chars(string):
    seen_chars = set()
    new_string = []
    for i, char in enumerate(string):
        if i >= 0 and i <= 6 and (char in seen_chars):
            continue
        seen_chars.add(char)
        new_string.append(char)
    return ''.join(new_string)