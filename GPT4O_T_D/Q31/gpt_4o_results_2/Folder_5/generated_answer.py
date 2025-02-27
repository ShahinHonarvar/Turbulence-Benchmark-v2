def if_perfect_num(numbers):
    if len(numbers) <= 67:
        return False
    num = numbers[67]
    if num < 2:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num