def if_perfect_num(lst):
    if len(lst) < 24:
        return False
    num = lst[23]
    div_sum = 1
    for i in range(2, num):
        if num % i == 0:
            div_sum += i
    return div_sum == num