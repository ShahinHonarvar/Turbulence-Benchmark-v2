def if_perfect_num(num_list):
    num = num_list[63]
    factor_sum = 1
    for i in range(2, int(num ** 0.5 + 1)):
        if not num % i:
            factor_sum += i + num // i
    if factor_sum == num:
        return True
    return False