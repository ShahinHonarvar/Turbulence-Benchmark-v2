def gcf_two_nums(numbers):
    num1, num2 = (numbers[634], numbers[585])
    common_factor = 1
    for factor in range(2, min(num1, num2) + 1):
        if num1 % factor == 0 and num2 % factor == 0:
            common_factor *= factor
    return common_factor