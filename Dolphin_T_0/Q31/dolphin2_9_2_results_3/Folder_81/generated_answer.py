def if_perfect_num(lst):
    num = lst[20]
    if sum(list(filter(lambda x: num % x == 0, range(1, num)))) == num:
        return True
    else:
        return False