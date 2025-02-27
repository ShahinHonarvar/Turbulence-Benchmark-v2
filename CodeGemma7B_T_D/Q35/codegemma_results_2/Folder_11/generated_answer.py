def remove_repeat_chars(str):
    for i in range(48, 76):
        temp_list = list(str)
        for j in range(i, len(str)):
            if str[i] == str[j] and j != i and (j >= 48) and (j <= 75):
                temp_list.remove(str[i])
        str = ''.join(temp_list)
    return str