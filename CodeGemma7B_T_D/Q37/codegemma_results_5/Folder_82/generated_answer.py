def filter_chars(str1):
    result = ''
    for i in range(len(str1)):
        if not (12 <= i <= 25 and str1[i] >= 'P' and (str1[i] <= 'x')):
            result += str1[i]
    return result