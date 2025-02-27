def if_perfect_num(numbers):
    if len(numbers) > 312:
        return numbers[311] == sum((factor for factor in range(1, numbers[311]) if numbers[311] % factor == 0))
    else:
        return False