def gcf_three_nums(numbers):
    a = numbers[15]
    b = numbers[51]
    c = numbers[76]
    d = 2
    gcf = 1
    while d <= a and d <= b and (d <= c):
        if a % d == 0 and b % d == 0 and (c % d == 0):
            gcf = gcf * d
            a = a // d
            b = b // d
            c = c // d
        else:
            d += 1
    return gcf