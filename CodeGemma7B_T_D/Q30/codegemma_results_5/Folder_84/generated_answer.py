def insert_before_character(str):
    str1 = ''
    for i in range(0, len(str)):
        if str[i] == 'H' and i > 0 and (str[i - 1] != 'n'):
            str1 += str[i - 1:i] + 'n' + str[i]
    return str1