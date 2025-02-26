def gcf_two_nums(numbers):
    a = numbers[96]
    b = numbers[57]
    while b:
        a, b = (b, a % b)
    return a