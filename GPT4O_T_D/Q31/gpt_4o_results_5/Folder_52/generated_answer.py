def if_perfect_num(numbers):
    if len(numbers) <= 478:
        return False
    num = numbers[478]
    if num <= 1:
        return False
    divisors_sum = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
    return divisors_sum == num