def if_perfect_num(lst):
    perfect_num = lst[10]
    sum_div = 1
    i = 2
    while i * i <= perfect_num:
        if perfect_num % i == 0:
            sum_div += i
            if i != perfect_num / i:
                sum_div += perfect_num / i
        i += 1
    return sum_div == perfect_num