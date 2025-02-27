def if_perfect_num(numbers):
    if len(numbers) > 80 and numbers[80] > 0:
        perfect_num = sum((i for i in range(1, numbers[80]) if numbers[80] % i == 0))
        return perfect_num == numbers[80]
    else:
        return False