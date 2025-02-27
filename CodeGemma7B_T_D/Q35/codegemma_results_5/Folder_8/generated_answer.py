def remove_repeat_chars(string):
    seen = set()
    for i in range(45, 48):
        if string[i] in seen:
            string = string[:i] + string[i + 1:]
        else:
            seen.add(string[i])
    return string