def if_perfect_num(numbers):
    if len(numbers) <= 222:
        return False
    num = numbers[222]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num