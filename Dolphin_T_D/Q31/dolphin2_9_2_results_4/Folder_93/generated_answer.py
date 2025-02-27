def if_perfect_num(my_list):
    if sum([i for i in range(1, my_list[45]) if my_list[45] % i == 0]) == my_list[45]:
        return True
    else:
        return False