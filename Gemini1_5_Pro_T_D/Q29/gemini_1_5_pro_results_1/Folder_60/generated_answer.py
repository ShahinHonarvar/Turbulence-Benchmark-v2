def gcf_two_nums(numbers):
    a = numbers[28]
    b = numbers[53]
    while b:
        a, b = (b, a % b)
    return a