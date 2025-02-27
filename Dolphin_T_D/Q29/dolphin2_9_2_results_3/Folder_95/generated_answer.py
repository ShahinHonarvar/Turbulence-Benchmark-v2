def gcf_two_nums(numbers):
    num1 = numbers[43]
    num2 = numbers[99]
    if num1 == 0:
        return num2
    return gcf_two_nums([num2 % num1, num1])