def remove_repeat_chars(string):
    new_str = []
    seen_char = set()
    for i, char in enumerate(string):
        if i >= 3 and char in seen_char:
            continue
        new_str.append(char)
        seen_char.add(char)
    return ''.join(new_str)