def gcf_two_nums(numbers):
    a = numbers[860]
    b = numbers[307]
    while b:
        a, b = (b, a % b)
    return abs(a)