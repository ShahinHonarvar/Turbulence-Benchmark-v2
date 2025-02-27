def if_perfect_num(integer_list):
    if len(integer_list) > 99 and integer_list[99] % sum([i for i in range(1, integer_list[99]) if integer_list[99] % i == 0]) == 0:
        return True
    else:
        return False