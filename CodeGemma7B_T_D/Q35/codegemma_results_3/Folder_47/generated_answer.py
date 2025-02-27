def remove_repeat_chars(str):
    str_list = list(str)
    for i in range(29, 54):
        shortest_length = len(str)
        char_to_remove = str[i]
        for j in range(i + 1, len(str)):
            if str[j] == char_to_remove:
                shortest_length -= 1
        for j in range(i + 1, len(str) - shortest_length + i + 1):
            str_list[j] = str_list[j + shortest_length]
    str = ''.join(str_list)
    return str