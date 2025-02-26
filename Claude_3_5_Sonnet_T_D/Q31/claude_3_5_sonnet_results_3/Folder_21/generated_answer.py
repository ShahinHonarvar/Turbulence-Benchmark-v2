def if_perfect_num(numbers):
    if len(numbers) <= 410:
        return False
    num = numbers[410]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num