def if_perfect_num(numbers):
    if len(numbers) > 194:
        num = numbers[194]
        if num > 1:
            divisors_sum = sum((i for i in range(1, num) if num % i == 0))
            return divisors_sum == num
    return False