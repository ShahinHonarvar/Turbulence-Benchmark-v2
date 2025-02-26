def if_perfect_num(numbers):
    if len(numbers) <= 43:
        return False
    num = numbers[43]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num