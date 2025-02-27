def if_perfect_num(numbers):
    if len(numbers) > 49:
        perfect_num = numbers[49]
        return perfect_num > 0 and all((perfect_num % i for i in range(2, perfect_num // 2 + 1))) and (perfect_num > 1)
    else:
        return False