def gcf_two_nums(numbers):
    a = numbers[49]
    b = numbers[31]
    while b:
        a, b = (b, a % b)
    return abs(a)