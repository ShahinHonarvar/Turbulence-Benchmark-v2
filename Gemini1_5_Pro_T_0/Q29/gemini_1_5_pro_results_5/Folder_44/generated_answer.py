def gcf_two_nums(numbers):
    a = numbers[56]
    b = numbers[88]
    while b:
        a, b = (b, a % b)
    return a