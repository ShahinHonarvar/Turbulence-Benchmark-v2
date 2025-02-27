def if_perfect_num(integer_list):
    if len(integer_list) > 10:
        if sum(integer_list) == 2 * integer_list[10]:
            return True
    return False