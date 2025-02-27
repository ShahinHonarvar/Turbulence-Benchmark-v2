def remove_repeat_chars(str):
    seen_chars = set()
    new_str = ''
    for i in range(57, 84):
        if str[i] not in seen_chars:
            seen_chars.add(str[i])
            new_str += str[i]
    return new_str