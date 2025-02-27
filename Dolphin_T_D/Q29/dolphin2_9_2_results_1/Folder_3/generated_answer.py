def gcf_two_nums(numbers):
    num1 = numbers[47]
    num2 = numbers[10]
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf