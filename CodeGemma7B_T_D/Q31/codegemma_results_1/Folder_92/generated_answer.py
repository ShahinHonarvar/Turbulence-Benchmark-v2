def is_perfect_num(list_num):
    if list_num[0] % sum(range(1, list_num[0])) == 0:
        return True
    else:
        return False