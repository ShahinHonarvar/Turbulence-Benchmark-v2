def gcf_two_nums(numbers):
    a = numbers[17]
    b = numbers[20]
    while b:
        a, b = (b, a % b)
    return abs(a)