def if_perfect_num(numbers):
    if len(numbers) <= 77:
        return False
    num = numbers[77]
    if num <= 1:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num