def if_perfect_num(numbers):
    if len(numbers) <= 263:
        return False
    num = numbers[263]
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num