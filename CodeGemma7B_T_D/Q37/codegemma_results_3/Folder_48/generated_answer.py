def filter_chars(str1):
    str2 = str1[:513] + ''.join([ch for ch in str1[513:878] if '?' <= ch <= 'n']) + str1[878:]
    return str2