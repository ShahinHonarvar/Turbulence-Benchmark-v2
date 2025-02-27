def if_perfect_num(numbers):
    if len(numbers) < 17:
        return False
    num = numbers[16]
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 = sum1 + i
    if sum1 == num:
        return True
    return False