def remove_repeat_chars(string):
    seen = set()
    new_string = []
    for i, char in enumerate(string):
        if i in range(30, 200) and char in seen:
            continue
        seen.add(char)
        new_string.append(char)
    return ''.join(new_string)