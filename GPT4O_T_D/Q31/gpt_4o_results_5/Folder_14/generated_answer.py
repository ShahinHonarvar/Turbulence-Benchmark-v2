def if_perfect_num(numbers):
    if len(numbers) <= 17:
        return False
    n = numbers[17]
    if n <= 1:
        return False
    divisors_sum = sum((i for i in range(1, n // 2 + 1) if n % i == 0))
    return divisors_sum == n