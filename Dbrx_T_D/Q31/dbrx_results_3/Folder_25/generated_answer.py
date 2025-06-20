def if_perfect_num(numbers):
    if len(numbers) > 90:
        target_number = numbers[90]
        sum_factors = sum((factor for factor in range(1, target_number) if target_number % factor == 0))
        return sum_factors == target_number
    else:
        return False