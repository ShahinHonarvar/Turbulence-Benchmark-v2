def if_perfect_num(num_list):
    if len(num_list) < 9:
        return False
    num = num_list[8]
    sum_factors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i == num / i:
                sum_factors = sum_factors + i
            else:
                sum_factors = sum_factors + i + num / i
    if sum_factors == num:
        return True
    else:
        return False