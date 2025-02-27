def is_perfect_number(n):
    if n < 2:
        return False
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n

def if_perfect_num(numbers):
    if len(numbers) > 73:
        return is_perfect_number(numbers[73])
    return False