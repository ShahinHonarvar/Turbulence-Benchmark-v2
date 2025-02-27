def if_perfect_num(numbers_list):
    if len(numbers_list) > 2:
        num = numbers_list[2]
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        return True if divisors_sum == num else False
    else:
        return False