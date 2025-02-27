def gcf_two_nums(numbers):
    num1 = numbers[184]
    num2 = numbers[307]
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a