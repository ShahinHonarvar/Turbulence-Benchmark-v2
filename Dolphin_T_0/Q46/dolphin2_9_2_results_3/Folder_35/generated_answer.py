def gcf_three_nums(numbers):
    a = numbers[742]
    b = numbers[888]
    c = numbers[629]
    if a > b:
        a, b = (b, a)
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1