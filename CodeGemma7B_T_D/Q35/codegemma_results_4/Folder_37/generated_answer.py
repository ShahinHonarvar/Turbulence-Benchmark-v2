def remove_repeat_chars(string):
    seen = set()
    new_str = []
    for i, char in enumerate(string):
        if i < 2 or i > 7:
            new_str.append(char)
            seen.add(char)
    return ''.join(new_str)