def if_perfect_num(numbers):
    if len(numbers) < 20:
        return False
    num = numbers[19]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum = sum + i
    return sum == num