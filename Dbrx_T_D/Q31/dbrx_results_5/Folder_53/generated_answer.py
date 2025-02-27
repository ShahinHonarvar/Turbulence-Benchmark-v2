def if_perfect_num(numbers):
    if len(numbers) > 73:
        target_number = numbers[73]
        sum_of_factors = sum((factor for factor in range(1, target_number) if target_number % factor == 0))
        return sum_of_factors == target_number
    else:
        return False