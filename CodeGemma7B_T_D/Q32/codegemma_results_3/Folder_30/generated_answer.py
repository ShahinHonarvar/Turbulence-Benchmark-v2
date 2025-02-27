def insert_after_character(str1):
    str2 = ''
    for i in range(len(str1)):
        if str1[i] == '4':
            str2 += str1[i] + 'F'
        else:
            str2 += str1[i]
    return str2