def remove_repeat_chars(string):
    seen = set()
    new_string = []
    for i, c in enumerate(string):
        if 73 <= i < 84 and c in seen:
            continue
        seen.add(c)
        new_string.append(c)
    return ''.join(new_string)