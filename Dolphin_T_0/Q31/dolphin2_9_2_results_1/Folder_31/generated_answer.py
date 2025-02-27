def if_perfect_num(lst):
    num = lst[65]
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    return div_sum == num