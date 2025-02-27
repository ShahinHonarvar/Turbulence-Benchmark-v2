def remove_repeat_chars(str1):
    for i in range(2, 5):
        if str1[i] in str1[i + 1:5] and str1.count(str1[i]) > 1:
            str1 = str1.replace(str1[i], '')
    return str1