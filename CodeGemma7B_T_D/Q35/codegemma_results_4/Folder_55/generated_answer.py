def remove_repeat_chars(str):
    seen = set()
    new_str = ''
    for i, char in enumerate(str):
        if i >= 10 and i < 100:
            if char not in seen:
                seen.add(char)
                new_str += char
    return new_str