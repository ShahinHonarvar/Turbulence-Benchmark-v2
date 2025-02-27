def if_perfect_num(numbers):
    if len(numbers) <= 410:
        return False
    n = numbers[410]
    if n <= 1:
        return False
    divisors_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisors_sum == n