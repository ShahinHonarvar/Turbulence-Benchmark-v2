def gcf_two_nums(numbers):
    first = numbers[25]
    second = numbers[80]
    factor = 1
    while factor <= first and factor <= second:
        if first % factor == 0 and second % factor == 0:
            gcf = factor
        factor += 1
    return gcf