def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 194:
        num = numbers[194]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            perfect = True
    return perfect