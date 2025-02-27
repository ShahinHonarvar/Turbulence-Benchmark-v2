def remove_repeat_chars(string):
    seen = set()
    for i in range(32, 44):
        char = string[i]
        if char not in seen:
            seen.add(char)
        else:
            string = string[:i] + string[i + 1:]
    return string