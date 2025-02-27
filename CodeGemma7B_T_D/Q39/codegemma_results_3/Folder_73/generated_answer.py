def return_n_greatest_chars(great_str):
    great_list = sorted(list(set(great_str)), reverse=True)[:80]
    return ''.join(great_list)