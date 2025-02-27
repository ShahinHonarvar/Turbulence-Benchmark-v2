def gcf_two_nums(numbers):
    num1 = numbers[29]
    num2 = numbers[74]
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            greatest_common_factor = i
    return greatest_common_factor