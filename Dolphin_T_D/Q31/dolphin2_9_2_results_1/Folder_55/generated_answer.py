def if_perfect_num(input_list):
    if len(input_list) > 21:
        if sum(input_list[21::-1]) == input_list[21]:
            return True
    return False