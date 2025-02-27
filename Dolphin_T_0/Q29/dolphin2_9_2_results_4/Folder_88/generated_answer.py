def gcf_two_nums(numbers):
    num1 = numbers[27]
    num2 = numbers[34]
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1