def remove_repeat_chars(string):
    repeat_chars = set()
    unique_chars = []
    for i, char in enumerate(string):
        if 86 < i < 99:
            if char in repeat_chars:
                continue
            repeat_chars.add(char)
        else:
            unique_chars.append(char)
    return ''.join(unique_chars)