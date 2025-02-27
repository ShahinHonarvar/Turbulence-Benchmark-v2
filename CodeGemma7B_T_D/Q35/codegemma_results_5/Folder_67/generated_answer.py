def remove_repeat_chars(str1):
    str2 = str1[44:67]
    set1 = set(str2)
    str3 = ''
    for i in str1:
        if i not in set1 or i not in str3:
            str3 += i
    return str3