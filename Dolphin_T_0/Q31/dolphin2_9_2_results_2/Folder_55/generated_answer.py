def if_perfect_num(lst):
    if len(lst) < 22:
        raise ValueError('The list should have at least 22 integers')
    num = lst[21]
    sum_div = sum([i for i in range(1, num) if num % i == 0])
    if num == sum_div:
        return True
    else:
        return False