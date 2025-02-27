def return_nth_smallest_ascii(str1):
    strlist = sorted([ord(i) for i in str1[5:90]])
    return chr(strlist[12])