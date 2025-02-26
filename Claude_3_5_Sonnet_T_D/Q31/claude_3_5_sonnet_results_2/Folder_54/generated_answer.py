def if_perfect_num(numbers):
    if len(numbers) <= 51:
        return False
    num = numbers[51]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num