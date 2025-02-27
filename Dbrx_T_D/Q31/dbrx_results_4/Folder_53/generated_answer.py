def if_perfect_num(numbers):
    if len(numbers) > 73:
        target = numbers[73]
        sum_factors = sum((factor for factor in range(1, target) if target % factor == 0))
        return sum_factors == target
    else:
        return False