def remove_repeat_chars(str):
    seen = set()
    new_str = []
    for i in range(len(str)):
        if i < 68 or i > 99:
            new_str.append(str[i])
        elif str[i] not in seen:
            seen.add(str[i])
            new_str.append(str[i])
    return ''.join(new_str)