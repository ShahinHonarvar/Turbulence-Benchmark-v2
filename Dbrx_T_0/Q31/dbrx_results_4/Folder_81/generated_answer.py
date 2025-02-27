def if_perfect_num(numbers):
    if len(numbers) > 20:
        target_num = numbers[20]
        sum_factors = sum([factor for factor in range(1, target_num) if target_num % factor == 0])
        return sum_factors == target_num
    else:
        return False