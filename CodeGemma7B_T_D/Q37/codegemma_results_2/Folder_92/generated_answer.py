def filter_chars(a):
    return ''.join(list(filter(lambda x: x not in '789:;<,>=?@#$%^&*()_-+' and x >= '7' and (x <= 'o'), a)))