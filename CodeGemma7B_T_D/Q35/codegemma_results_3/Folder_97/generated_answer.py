def remove_repeat_chars(str):
    seen_chars = set()
    new_str = []
    for i, char in enumerate(str):
        if i < 34 or i >= 69:
            continue
        if char in seen_chars:
            continue
        seen_chars.add(char)
        new_str.append(char)
    return ''.join(new_str)