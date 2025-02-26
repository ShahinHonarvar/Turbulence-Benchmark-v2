def if_perfect_num(numbers):
    if len(numbers) <= 53:
        return False
    num = numbers[53]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num