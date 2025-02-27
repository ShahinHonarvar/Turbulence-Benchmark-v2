def gcf_two_nums(numbers):
    a = numbers[793]
    b = numbers[449]
    while b:
        a, b = (b, a % b)
    return a