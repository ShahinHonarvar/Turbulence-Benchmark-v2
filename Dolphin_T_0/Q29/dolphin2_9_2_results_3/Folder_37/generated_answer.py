def gcf_two_nums(numbers):
    a = numbers[29]
    b = numbers[74]
    while b != 0:
        a, b = (b, a % b)
    return a