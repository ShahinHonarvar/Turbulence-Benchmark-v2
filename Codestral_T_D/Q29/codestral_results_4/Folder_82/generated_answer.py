def gcf_two_nums(numbers):
    a = numbers[33]
    b = numbers[72]
    while b != 0:
        a, b = (b, a % b)
    return a