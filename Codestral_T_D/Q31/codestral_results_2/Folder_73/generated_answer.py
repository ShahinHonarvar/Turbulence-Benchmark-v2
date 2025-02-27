def if_perfect_num(numbers):
    i = 41
    sum = 0
    for x in range(1, numbers[i]):
        if numbers[i] % x == 0:
            sum += x
    return sum == numbers[i]