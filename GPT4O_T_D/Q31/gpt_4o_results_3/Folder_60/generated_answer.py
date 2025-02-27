def if_perfect_num(numbers):
    if len(numbers) <= 88:
        return False
    number = numbers[88]
    if number <= 1:
        return False
    sum_divisors = sum((i for i in range(1, number) if number % i == 0))
    return sum_divisors == number