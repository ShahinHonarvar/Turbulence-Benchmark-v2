def remove_repeat_chars(str1):
    for i in range(80, 200):
        for j in range(i + 1, len(str1)):
            if str1[i] > str1[j]:
                str1 = str1[:j] + str1[j + 1:]
    return str1