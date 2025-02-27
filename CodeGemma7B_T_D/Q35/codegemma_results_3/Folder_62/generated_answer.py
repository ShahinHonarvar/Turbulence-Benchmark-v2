def remove_repeat_chars(str):
    for i in range(50, 92):
        for k in str[i + 1:]:
            if k == str[i]:
                str = str.replace(str[i], '')
    return str