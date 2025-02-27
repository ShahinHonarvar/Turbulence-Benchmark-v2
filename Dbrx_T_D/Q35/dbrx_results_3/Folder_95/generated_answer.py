def remove_repeat_chars(string):
    seen_chars = set()
    unique_chars = []
    for i in range(len(string)):
        if i < 32 or i > 98:
            unique_chars.append(string[i])
        elif string[i] not in seen_chars:
            unique_chars.append(string[i])
            seen_chars.add(string[i])
    return ''.join(unique_chars)