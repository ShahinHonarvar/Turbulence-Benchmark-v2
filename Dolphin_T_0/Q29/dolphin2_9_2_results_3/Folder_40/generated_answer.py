def gcf_two_nums(numbers):
    num1 = numbers[7]
    num2 = numbers[9]
    gcf = min([num1, num2])
    for i in range(1, gcf + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf