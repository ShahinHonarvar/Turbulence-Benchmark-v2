def remove_repeat_chars(str1):
    for i in range(20, 51):
        for j in range(i + 1, 51):
            if str1[i] == str1[j]:
                for k in range(j, 51)[::-1]:
                    str1 = str1[:k] + str1[k + 1:]
    return str1