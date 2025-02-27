def if_perfect_num(list_of_int):
    if sum([int(i) for i in str(list_of_int[100])]) == 100:
        return True
    else:
        return False