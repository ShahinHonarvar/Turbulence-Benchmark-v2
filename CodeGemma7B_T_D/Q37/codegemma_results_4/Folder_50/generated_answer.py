def filter_chars(str1):
    new_str = ''
    for i in range(71, 97):
        if str1[i] >= '_' and str1[i] <= 'o':
            continue
        new_str += str1[i]
    return new_str