def gcf_three_nums(numbers):
    num1 = numbers[91]
    num2 = numbers[45]
    num3 = numbers[48]
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    if num3 > greater:
        greater = num3
    for i in range(1, greater + 1):
        if greater % num1 == 0 and greater % num2 == 0 and (greater % num3 == 0):
            return i