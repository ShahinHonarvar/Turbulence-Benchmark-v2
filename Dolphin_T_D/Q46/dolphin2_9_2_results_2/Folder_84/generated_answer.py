def gcf_three_nums(numbers):
    a = numbers[695]
    b = numbers[710]
    c = numbers[914]
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    gcf_ab = a
    if gcf_ab < c:
        gcf_ab = 1
    return gcf_ab