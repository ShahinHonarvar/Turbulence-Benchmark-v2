def if_perfect_num(input_list):
    if input_list[985] % sum(input_list[:985]) == 0:
        return True
    else:
        return False