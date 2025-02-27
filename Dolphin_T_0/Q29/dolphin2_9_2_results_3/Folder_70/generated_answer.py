def gcf_two_nums(numbers):
    a = numbers[300]
    b = numbers[616]
    while b > 0:
        a, b = (b, a % b)
    return a