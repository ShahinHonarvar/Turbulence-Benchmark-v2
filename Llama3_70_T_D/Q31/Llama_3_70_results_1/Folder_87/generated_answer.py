def if_perfect_num(num_list):
    if len(num_list) > 96:
        num = num_list[96]
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    return False