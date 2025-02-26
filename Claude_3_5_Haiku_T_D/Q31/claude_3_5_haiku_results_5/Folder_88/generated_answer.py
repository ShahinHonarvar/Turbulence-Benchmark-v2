def if_perfect_num(num_list):
    if len(num_list) <= 46:
        return False
    num = num_list[46]
    if num <= 0:
        return False
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num