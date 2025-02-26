def gcf_two_nums(numbers):
    a, b = (numbers[1], numbers[2])
    while b:
        a, b = (b, a % b)
    return a