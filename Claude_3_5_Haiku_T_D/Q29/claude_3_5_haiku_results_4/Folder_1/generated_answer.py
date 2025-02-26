def gcf_two_nums(numbers):
    a = numbers[13]
    b = numbers[66]
    while b:
        a, b = (b, a % b)
    return a