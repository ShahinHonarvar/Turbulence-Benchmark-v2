def if_perfect_num(numbers):
    if len(numbers) > 410:
        num = numbers[410]
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    return False