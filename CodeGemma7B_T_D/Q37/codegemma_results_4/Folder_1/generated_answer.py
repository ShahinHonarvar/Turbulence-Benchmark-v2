def filter_chars(user_string):
    filter_list = list(range(41, 80))
    return ''.join([i for i in user_string if ord(i) not in filter_list or not 'f' <= i <= '|'])