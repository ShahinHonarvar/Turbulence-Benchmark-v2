def gcf_two_nums(numbers):
    a = numbers[23]
    b = numbers[27]
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a