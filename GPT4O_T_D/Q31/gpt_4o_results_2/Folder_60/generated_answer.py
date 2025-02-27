def if_perfect_num(numbers):
    if len(numbers) <= 88:
        return False
    n = numbers[88]
    if n < 2:
        return False
    divisors_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisors_sum == n