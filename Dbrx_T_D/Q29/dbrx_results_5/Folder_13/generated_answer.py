def gcf_two_nums(numbers):
    num1 = numbers[534]
    num2 = numbers[630]
    factor = 1
    for i in range(2, min(num1, num2) // 2 + 1):
        if num1 % i == 0 and num2 % i == 0:
            factor = i
    return factor