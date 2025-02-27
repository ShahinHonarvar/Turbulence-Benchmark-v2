def gcf_two_nums(numbers):
    a = numbers[1]
    b = numbers[2]
    while b:
        a, b = (b, a % b)
    return a