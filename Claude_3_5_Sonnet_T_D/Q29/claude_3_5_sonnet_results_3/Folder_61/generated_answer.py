def gcf_two_nums(numbers):
    a, b = (numbers[8], numbers[3])
    while b:
        a, b = (b, a % b)
    return a