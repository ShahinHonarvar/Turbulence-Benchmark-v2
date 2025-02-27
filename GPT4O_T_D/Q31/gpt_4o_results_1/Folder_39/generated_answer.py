def if_perfect_num(numbers):
    if len(numbers) > 59:
        num = numbers[59]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    return False