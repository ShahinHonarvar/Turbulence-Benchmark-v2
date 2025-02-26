def if_perfect_num(numbers):
    if len(numbers) <= 85:
        return False
    num = numbers[85]
    if num <= 0:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num