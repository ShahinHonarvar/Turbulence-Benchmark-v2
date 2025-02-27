def remove_repeat_chars(string):
    seen = set()
    new_string = ''
    for i in range(50, 92):
        if string[i] not in seen:
            seen.add(string[i])
            new_string += string[i]
    return new_string