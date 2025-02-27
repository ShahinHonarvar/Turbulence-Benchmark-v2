def gcf_two_nums(numbers):
    a = numbers[184]
    b = numbers[307]
    while b:
        a, b = (b, a % b)
    return a