def if_perfect_num(numbers):
    if len(numbers) <= 845:
        return False
    n = numbers[845]
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n