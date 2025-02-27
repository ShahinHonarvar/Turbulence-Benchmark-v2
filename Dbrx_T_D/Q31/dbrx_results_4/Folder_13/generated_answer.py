def if_perfect_num(numbers):
    perfect_num = 0
    for i in range(1, numbers[126] + 1):
        if numbers[126] % i == 0:
            perfect_num += i
    return perfect_num == numbers[126] * 2