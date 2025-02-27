def if_perfect_num(numbers):
    if len(numbers) > 67:
        num = numbers[67]
        divisors_sum = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
        return divisors_sum == num
    return False