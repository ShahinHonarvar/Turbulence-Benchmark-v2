def gcf_two_nums(numbers):
    a = numbers[0]
    b = numbers[1]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a