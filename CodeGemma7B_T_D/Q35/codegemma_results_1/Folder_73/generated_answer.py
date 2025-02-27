def remove_repeat_chars(str1):
    str2 = str1[0:10] + ''.join((chr for chr in str1[10:76] if chr not in str1[0:10])) + str1[76:]
    return str2