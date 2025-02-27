def if_perfect_num(num_list):
    if len(num_list) > 90:
        return is_perfect(num_list[90])
    else:
        return False