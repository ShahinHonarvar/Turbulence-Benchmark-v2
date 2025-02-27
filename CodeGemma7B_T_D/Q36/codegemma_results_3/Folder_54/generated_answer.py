def filter_chars(str_):
    for i in range(18, 38):
        if str_[i] > ')' and str_[i] < 'P':
            while str_.count(str_[i]):
                str_ = str_.replace(str_[i], '')
    return str_