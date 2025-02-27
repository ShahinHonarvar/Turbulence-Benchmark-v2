def remove_repeat_chars(string):
    for i in range(409, 502):
        c = string[i]
        while i + 1 < len(string) and string[i + 1] == c:
            string = string[:i] + string[i + 1:]
    return string