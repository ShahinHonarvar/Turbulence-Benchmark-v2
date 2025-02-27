def gcf_two_nums(numbers):
    a = numbers[372]
    b = numbers[752]
    while b:
        a, b = (b, a % b)
    return a