def remove_repeat_chars(s):
    seen = set()
    new_str = []
    for i, char in enumerate(s):
        if i < 49 or i >= 74:
            continue
        if char not in seen:
            seen.add(char)
            new_str.append(char)
    return ''.join(new_str)