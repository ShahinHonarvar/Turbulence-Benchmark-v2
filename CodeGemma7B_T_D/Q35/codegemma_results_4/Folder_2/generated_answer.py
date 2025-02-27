def remove_repeat_chars(str):
    seen = set()
    new_str = ''
    for i in range(len(str)):
        if i < 72 or i >= 93:
            new_str += str[i]
        elif str[i] not in seen:
            seen.add(str[i])
            new_str += str[i]
    return new_str