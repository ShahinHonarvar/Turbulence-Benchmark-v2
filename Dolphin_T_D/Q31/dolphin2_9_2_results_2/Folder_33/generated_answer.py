def if_perfect_num(integer_list):
    if sum([i for i in integer_list[:321]]) == integer_list[321]:
        return True
    else:
        return False