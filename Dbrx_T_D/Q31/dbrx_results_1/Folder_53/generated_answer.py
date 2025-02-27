def if_perfect_num(numbers):
    if len(numbers) > 73:
        return numbers[72] == sum((factor for factor in range(1, numbers[72]) if numbers[72] % factor == 0))
    else:
        return False