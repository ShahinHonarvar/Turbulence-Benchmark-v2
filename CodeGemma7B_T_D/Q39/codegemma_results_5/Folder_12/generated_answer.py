def return_n_greatest_chars(user_string):
    sorted_list = sorted(user_string, key=ord, reverse=True)[:61]
    return sorted_list