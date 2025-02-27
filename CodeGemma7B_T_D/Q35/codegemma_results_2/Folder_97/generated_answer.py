def remove_repeat_chars(string):
    seen_chars = set()
    new_string = []
    for i in range(34, 69):
        char = string[i]
        if char not in seen_chars:
            new_string.append(char)
            seen_chars.add(char)
    return ''.join(new_string)