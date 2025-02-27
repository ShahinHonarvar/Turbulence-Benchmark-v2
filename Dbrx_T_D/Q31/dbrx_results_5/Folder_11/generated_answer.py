def if_perfect_num(numbers):
    if len(numbers) > 77:
        target_num = numbers[77]
        return sum((i for i in range(1, target_num) if target_num % i == 0)) == target_num
    else:
        return False