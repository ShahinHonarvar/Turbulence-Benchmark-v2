def filter_chars(my_str):
    filtered_str = my_str[:318] + ''.join([ch for ch in my_str[318:337] if not 'B' <= ch <= 'z'], my_str[337:])
    return filtered_str