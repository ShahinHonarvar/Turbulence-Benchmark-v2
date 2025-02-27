def if_perfect_num(numbers):
    if len(numbers) <= 59:
        return False
    num = numbers[59]
    if num <= 1:
        return False
    sum_of_divisors = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num