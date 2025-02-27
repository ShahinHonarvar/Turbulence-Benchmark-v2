def if_perfect_num(int_list):
    if sum((int_list[851] // i for i in range(1, int_list[851]))) == int_list[851]:
        return True
    else:
        return False