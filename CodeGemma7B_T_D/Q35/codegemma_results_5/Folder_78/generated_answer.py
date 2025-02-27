def remove_repeat_chars(string):
    seen_chars = set()
    new_string = ''
    for i in range(len(string)):
        if i in range(63, 97):
            if string[i] not in seen_chars:
                new_string += string[i]
                seen_chars.add(string[i])
    return new_string