def remove_repeat_chars(s):
    seen = set()
    unique = ''
    for i, char in enumerate(s):
        if i >= 6 and i < 9:
            if char not in seen:
                unique += char
            seen.add(char)
        else:
            unique += char
    return unique