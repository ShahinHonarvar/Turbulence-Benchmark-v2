def if_perfect_num(numbers):
    if len(numbers) < 4:
        return False
    num = numbers[3]
    if num < 1:
        return False
    sum_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_factors += i
    return sum_factors == num