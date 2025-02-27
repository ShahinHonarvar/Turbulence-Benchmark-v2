def if_perfect_num(numbers):
    if len(numbers) <= 38:
        return False
    n = numbers[38]
    divisors_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisors_sum == n