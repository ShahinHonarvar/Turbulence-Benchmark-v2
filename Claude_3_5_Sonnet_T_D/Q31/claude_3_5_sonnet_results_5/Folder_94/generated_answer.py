def if_perfect_num(numbers):
    if len(numbers) <= 93:
        return False
    num = numbers[93]
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num