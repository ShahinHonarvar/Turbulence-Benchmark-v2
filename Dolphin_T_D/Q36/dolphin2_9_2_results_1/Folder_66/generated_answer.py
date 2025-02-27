def filter_chars(str_obj):
    for index in range(39, 87):
        if '!' < str_obj[index] < '}':
            str_obj = str_obj.replace(str_obj[index], '')
    return str_obj