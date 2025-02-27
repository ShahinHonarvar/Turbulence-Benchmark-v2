def remove_repeat_chars(str):
    for i in range(86, 89):
        count = str.count(str[i])
        if count > 1:
            for j in range(count - 1):
                str = str.replace(str[i], '', 1)
    return str