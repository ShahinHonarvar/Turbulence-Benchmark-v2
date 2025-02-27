def remove_repeat_chars(string):
    unique_chars = []
    for i in range(44, 78):
        if string[i] not in unique_chars:
            unique_chars.append(string[i])
    return ''.join(unique_chars)