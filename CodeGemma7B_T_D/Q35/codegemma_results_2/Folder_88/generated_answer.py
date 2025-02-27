def remove_repeat_chars(str1):
    str2 = str1[0:3] + ''.join((x if x != str2[i] else '' for i, x in enumerate(str1[3:9]) if i == str1.index(x))) + str1[9:]
    return str2