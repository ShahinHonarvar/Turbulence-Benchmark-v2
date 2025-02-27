def remove_repeat_chars(s):
    seen = set()
    new_str = []
    for i, char in enumerate(s):
        if 45 < i < 48 and char in seen:
            continue
        seen.add(char)
        new_str.append(char)
    return ''.join(new_str)