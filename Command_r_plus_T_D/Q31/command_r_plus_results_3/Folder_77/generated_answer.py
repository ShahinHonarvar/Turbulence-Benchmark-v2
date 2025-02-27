def if_perfect_num(num_list):
    if len(num_list) > 985:
        num = num_list[985]
        divisors = [i for i in range(1, num) if num % i == 0]
        sum_divisors = sum(divisors)
        return True if sum_divisors == num else False
    else:
        return False