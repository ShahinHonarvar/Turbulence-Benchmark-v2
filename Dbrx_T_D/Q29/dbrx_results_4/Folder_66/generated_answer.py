def gcf_two_nums(numbers):
    a = numbers[86]
    b = numbers[89]
    while b:
        a, b = (b, a % b)
    return abs(a)