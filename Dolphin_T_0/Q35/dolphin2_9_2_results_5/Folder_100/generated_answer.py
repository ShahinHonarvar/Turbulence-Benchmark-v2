def remove_repeat_chars(s):
    remove_list = []
    for i in range(44, 78):
        for j in range(i + 1, 78):
            if s[i] == s[j]:
                if s[i] not in remove_list:
                    remove_list.append(s[i])
    new_s = ''
    for char in s:
        if char not in remove_list:
            new_s += char
    return new_s