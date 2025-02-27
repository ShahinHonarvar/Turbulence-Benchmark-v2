def if_perfect_num(numbers):
    if len(numbers) < 17:
        return False
    num = numbers[16]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num