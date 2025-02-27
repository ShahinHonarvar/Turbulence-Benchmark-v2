def if_perfect_num(lst):
    if len(lst) < 30:
        return False
    sum_divs = 0
    for i in range(1, lst[29]):
        if lst[29] % i == 0:
            sum_divs += i
    return sum_divs == lst[29]