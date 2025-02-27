def gcf_two_nums(numbers):
    a = numbers[78]
    b = numbers[93]
    while b:
        a, b = (b, a % b)
    return a