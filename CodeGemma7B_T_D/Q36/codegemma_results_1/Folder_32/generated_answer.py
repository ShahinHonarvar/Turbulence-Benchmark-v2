def filter_chars(str1):
    result = ''
    for i in range(len(str1)):
        if i not in range(40, 63):
            if i >= 7 and i <= 8:
                continue
            result += str1[i]
    return result