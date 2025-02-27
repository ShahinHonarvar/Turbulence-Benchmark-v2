def gcf_two_nums(numbers):
    a = numbers[69]
    b = numbers[40]
    while b:
        a, b = (b, a % b)
    return a