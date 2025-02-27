def gcf_two_nums(numbers):
    a = numbers[27]
    b = numbers[34]
    while b != 0:
        a, b = (b, a % b)
    return a