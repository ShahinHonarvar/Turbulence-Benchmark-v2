def if_perfect_num(numbers):
    if len(numbers) > 60 and numbers[60] % 2 == 0 and (sum([i for i in range(1, numbers[60]) if numbers[60] % i == 0 and numbers[60] / i != i]) == numbers[60]):
        return True
    return False