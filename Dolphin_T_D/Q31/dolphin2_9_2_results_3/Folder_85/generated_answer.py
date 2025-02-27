def if_perfect_num(lst):
    perfect_num = lst[23]
    div_sum = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            div_sum += i
    return div_sum == perfect_num