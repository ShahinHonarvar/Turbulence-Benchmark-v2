def remove_repeat_chars(str):
    seen = set()
    new_str = []
    for i in range(len(str)):
        if i < 10 and str[i] in seen:
            continue
        seen.add(str[i])
        new_str.append(str[i])
    return ''.join(new_str)