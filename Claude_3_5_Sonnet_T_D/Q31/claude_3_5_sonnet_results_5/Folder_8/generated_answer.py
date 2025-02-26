def if_perfect_num(numbers):
    if len(numbers) <= 49:
        return False
    num = numbers[49]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num