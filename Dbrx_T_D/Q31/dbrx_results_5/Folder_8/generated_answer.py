def if_perfect_num(numbers):
    if len(numbers) > 49:
        target_num = numbers[49]
        sum_factors = sum([i for i in range(1, target_num) if target_num % i == 0])
        return sum_factors == target_num
    else:
        return False