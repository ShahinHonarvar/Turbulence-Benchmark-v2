def gcf_two_nums(numbers):
    num1 = numbers[24]
    num2 = numbers[68]
    for factor in set(range(1, min(num1, num2) + 1)):
        if num1 % factor == 0 and num2 % factor == 0:
            greatest_factor = factor
    return greatest_factor