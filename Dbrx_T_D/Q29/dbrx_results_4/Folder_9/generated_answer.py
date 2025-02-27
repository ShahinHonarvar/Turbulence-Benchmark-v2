def gcf_two_nums(numbers):
    a = numbers[84]
    b = numbers[63]
    while b:
        a, b = (b, a % b)
    return a