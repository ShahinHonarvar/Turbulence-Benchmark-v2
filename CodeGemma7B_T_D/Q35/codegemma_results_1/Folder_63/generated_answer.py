def remove_repeat_chars(string):
    seen = set()
    new_string = ''
    for i in range(len(string)):
        if i >= 81 and i <= 86:
            if string[i] not in seen:
                seen.add(string[i])
                new_string += string[i]
        else:
            new_string += string[i]
    return new_string