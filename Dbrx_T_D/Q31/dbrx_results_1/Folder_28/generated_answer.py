def if_perfect_num(numbers):
    if len(numbers) > 37 and numbers[37] % 2 == 0:
        sum_factors = sum([factor for factor in range(1, numbers[37] // 2 + 1) if numbers[37] % factor == 0])
        return sum_factors == numbers[37]
    elif len(numbers) > 37 and numbers[37] % 2 != 0:
        return False
    else:
        return None