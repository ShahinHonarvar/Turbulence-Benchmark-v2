def return_nth_smallest_ascii(s):
    char_list = []
    for i in range(17, 66):
        if s[i] not in char_list:
            char_list.append(s[i])
    char_list.sort()
    if len(char_list) >= 8:
        return char_list[7]
    else:
        return None