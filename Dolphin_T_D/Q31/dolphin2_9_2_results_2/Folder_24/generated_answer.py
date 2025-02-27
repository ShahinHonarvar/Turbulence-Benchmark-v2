def if_perfect_num(numbers):
    if len(numbers) < 75:
        return False
    num = numbers[74]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum == num