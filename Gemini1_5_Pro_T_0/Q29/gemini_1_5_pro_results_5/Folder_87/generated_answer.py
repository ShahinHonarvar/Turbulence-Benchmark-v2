def gcf_two_nums(numbers):
    a = numbers[83]
    b = numbers[14]
    while b:
        a, b = (b, a % b)
    return a