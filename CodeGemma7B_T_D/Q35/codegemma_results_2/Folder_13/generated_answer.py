def remove_repeat_chars(str1):
    str2 = ''
    for i in range(len(str1)):
        if str1[i] not in str2 and (i < 46 or i >= 91):
            str2 += str1[i]
    return str2