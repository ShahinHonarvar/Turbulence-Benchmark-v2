def if_perfect_num(numbers):
    if len(numbers) <= 126:
        return False
    num = numbers[126]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num