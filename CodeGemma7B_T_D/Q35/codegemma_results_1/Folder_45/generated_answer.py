def remove_repeat_chars(str):
    seen_chars = set()
    new_str = []
    for i in range(len(str)):
        if i < 40 or i >= 200:
            if str[i] not in seen_chars:
                seen_chars.add(str[i])
                new_str.append(str[i])
    return ''.join(new_str)