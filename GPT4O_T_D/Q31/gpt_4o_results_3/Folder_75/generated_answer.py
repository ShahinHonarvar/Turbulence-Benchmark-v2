def if_perfect_num(numbers):
    if len(numbers) <= 80:
        return False
    n = numbers[80]
    if n <= 1:
        return False
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n