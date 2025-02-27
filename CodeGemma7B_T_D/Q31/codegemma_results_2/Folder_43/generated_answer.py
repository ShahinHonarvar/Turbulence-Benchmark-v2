def if_perfect_num(list):
    x = list[29]
    for i in range(2, x):
        if x % i == 0:
            return False
    return True