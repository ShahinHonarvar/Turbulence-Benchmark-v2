def if_perfect_num(num_list):
    if len(num_list) > 34:
        num = num_list[34]
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return True if sum_divisors == num else False
    else:
        return False