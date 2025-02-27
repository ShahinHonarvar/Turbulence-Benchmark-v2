def gcf_two_nums(numbers):
    num1 = numbers[279]
    num2 = numbers[812]
    for factor in range(num1, 0, -1):
        if num1 % factor == 0 and num2 % factor == 0:
            return factor