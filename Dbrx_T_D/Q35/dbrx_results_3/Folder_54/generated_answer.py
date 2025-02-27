def remove_repeat_chars(string):
    used = set()
    unique = []
    for i in range(len(string)):
        if i >= 35 and i < 64:
            if string[i] not in used:
                unique.append(string[i])
                used.add(string[i])
        else:
            unique.append(string[i])
    return ''.join(unique)