def is_perfect_num(numbers):
    if len(numbers) < 8:
        return False
    proper_divisors = set([i for i in range(1, numbers[7]) if numbers[7] % i == 0])
    return sum(proper_divisors) == numbers[7]