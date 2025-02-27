def if_perfect_num(numbers_list):
    if len(numbers_list) > 132 and numbers_list[132] > 0:
        num = numbers_list[132]
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    return False