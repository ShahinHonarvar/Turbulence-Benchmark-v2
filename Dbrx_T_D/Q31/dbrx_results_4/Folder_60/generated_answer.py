def if_perfect_num(numbers):
    if len(numbers) > 88:
        target_number = numbers[88]
        return sum((factor for factor in range(1, target_number) if target_number % factor == 0)) == target_number
    else:
        return False