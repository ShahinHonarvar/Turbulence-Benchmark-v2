def gcf_two_nums(numbers):
    a = numbers[429]
    b = numbers[289]
    while b:
        a, b = (b, a % b)
    return a