def gcf_two_nums(numbers):
    a = numbers[8]
    b = numbers[3]
    while b:
        a, b = (b, a % b)
    return a