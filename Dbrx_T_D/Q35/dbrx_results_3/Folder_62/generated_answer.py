def remove_repeat_chars(string):
    seen_chars = set()
    result = ''
    for i in range(len(string)):
        if i >= 50 and i < 92:
            if string[i] in seen_chars:
                continue
            else:
                seen_chars.add(string[i])
        result += string[i]
    return result