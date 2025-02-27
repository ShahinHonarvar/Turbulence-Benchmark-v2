def if_perfect_num(numbers):
    if len(numbers) <= 96:
        return False
    num = numbers[96]
    if num <= 1:
        return False
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num