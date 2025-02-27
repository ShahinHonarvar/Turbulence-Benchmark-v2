def gcf_three_nums(numbers):
    a = numbers[99]
    b = numbers[95]
    c = numbers[80]
    gcf = a
    for factor in range(1, min(b, c) + 1):
        if a % factor == b % factor == c % factor == 0:
            gcf = factor
    return gcf