def if_perfect_num(num_list):
    if len(num_list) > 18:
        num = num_list[18]
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    return False