def remove_repeat_chars(str):
    for i in range(450, 905):
        if str[i] in str[450:905]:
            str = str.replace(str[i], '')
    return str