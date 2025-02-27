def return_n_greatest_chars(s):
    try:
        s_list = sorted(s, reverse=True)[:44]
        return s_list
    except TypeError:
        print('Please provide a string of distinct characters')