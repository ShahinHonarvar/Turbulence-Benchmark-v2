def gcf_three_nums(numbers):
    a, b, c = (numbers[477], numbers[696], numbers[663])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return abs(a)