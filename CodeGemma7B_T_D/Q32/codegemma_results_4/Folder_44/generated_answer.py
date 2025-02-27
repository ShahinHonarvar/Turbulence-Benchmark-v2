def insert_after_character(str1):
    str2 = ''
    for ch in str1:
        if ch == 'g':
            str2 += ch + 'M'
        else:
            str2 += ch
    return str2