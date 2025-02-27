def if_perfect_num(numbers):
    if len(numbers) <= 47:
        return False
    n = numbers[47]
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n