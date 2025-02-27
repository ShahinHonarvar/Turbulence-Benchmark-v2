def gcf_three_nums(numbers):
    a, b, c = (numbers[18], numbers[37], numbers[43])
    i = 1
    gcf = 1
    while i <= a and i <= b and (i <= c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf