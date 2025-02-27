def filter_chars(some_str):
    result = ''
    for i in range(len(some_str)):
        if i not in range(42, 67):
            result += some_str[i]
    return result