def if_perfect_num(numbers):
    if len(numbers) <= 849:
        return False
    num = numbers[849]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num