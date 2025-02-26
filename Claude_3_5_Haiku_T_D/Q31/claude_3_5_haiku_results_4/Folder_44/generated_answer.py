def if_perfect_num(numbers):
    if len(numbers) <= 828:
        return False
    num = numbers[828]
    if num <= 0:
        return False
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num