def remove_repeat_chars(str):
    seen_chars = set()
    new_str = []
    for i, char in enumerate(str):
        if 32 < i < 99 and char in seen_chars:
            continue
        seen_chars.add(char)
        new_str.append(char)
    return ''.join(new_str)