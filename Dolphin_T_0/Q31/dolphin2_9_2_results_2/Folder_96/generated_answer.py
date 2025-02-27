def if_perfect_num(int_list):
    num = int_list[47]
    sum_div = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_div += i
    return sum_div == num