def if_perfect_num(numbers):
    if len(numbers) > 6:
        perfect_num = sum((i for i in range(1, numbers[6]) if numbers[6] % i == 0))
        return perfect_num == numbers[6]
    else:
        return False