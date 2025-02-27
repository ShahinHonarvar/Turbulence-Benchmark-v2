def gcf_three_nums(numbers):
    num1, num2, num3 = (numbers[19], numbers[94], numbers[78])
    min_num = min(num1, num2, num3)
    gcf = 1
    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf