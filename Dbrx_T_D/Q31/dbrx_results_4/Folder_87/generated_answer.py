def if_perfect_num(numbers):
    if len(numbers) > 96:
        target_number = numbers[96]
        return sum((factor for factor in range(1, target_number) if target_number % factor == 0)) == target_number
    else:
        return False