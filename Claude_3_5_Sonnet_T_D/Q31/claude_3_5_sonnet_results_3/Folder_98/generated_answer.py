def if_perfect_num(numbers):
    if len(numbers) < 5:
        return False
    num = numbers[4]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num