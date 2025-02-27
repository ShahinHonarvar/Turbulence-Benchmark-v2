def return_n_greatest_chars(str):
    sorted_dec_list = sorted(str, key=ord, reverse=True)[:12]
    sorted_inc_list = sorted(str, key=ord, reverse=False)[:12]
    return (sorted_dec_list, sorted_inc_list)