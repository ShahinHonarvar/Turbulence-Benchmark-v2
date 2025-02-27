def if_perfect_num(my_list):
    if len(my_list) < 21:
        return False
    perfect_num = sum(my_list[:20])
    if perfect_num == my_list[20]:
        return True
    else:
        return False