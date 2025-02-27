def if_perfect_num(numbers):
    if len(numbers) > 23:
        target_num = numbers[23]
        return sum((factor for factor in range(1, target_num) if target_num % factor == 0)) == target_num
    else:
        return False