def if_perfect_num(numbers):
    if len(numbers) > 93:
        target_number = numbers[93]
        sum_of_factors = sum((factor for factor in range(1, target_number) if target_number % factor == 0))
        return sum_of_factors == target_number
    else:
        return False