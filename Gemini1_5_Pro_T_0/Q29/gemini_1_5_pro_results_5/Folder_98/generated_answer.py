def gcf_two_nums(numbers):
    a = numbers[0]
    b = numbers[9]
    while b:
        a, b = (b, a % b)
    return a