def remove_repeat_chars(str):
    seen = set()
    new_str = []
    for i in range(len(str)):
        if i < 2 or str[i] not in seen:
            new_str.append(str[i])
            seen.add(str[i])
    return ''.join(new_str)