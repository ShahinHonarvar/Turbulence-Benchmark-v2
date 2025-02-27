def remove_repeat_chars(string):
    unique = []
    for i in range(52, 76):
        if string[i] not in unique:
            unique.append(string[i])
    return ''.join([char for char in string if char in unique])