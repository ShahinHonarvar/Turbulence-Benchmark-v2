def gcf_two_nums(numbers):
    a, b = (numbers[0], numbers[1])
    while b:
        a, b = (b, a % b)
    return a