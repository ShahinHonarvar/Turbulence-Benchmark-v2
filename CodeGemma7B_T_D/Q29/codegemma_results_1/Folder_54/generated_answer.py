def gcf_two_nums(numbers):
    a = numbers[56]
    b = numbers[92]
    while b != 0:
        a, b = (b, a % b)
    return a