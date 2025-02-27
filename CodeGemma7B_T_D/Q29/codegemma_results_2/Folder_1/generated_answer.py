def gcf_two_nums(numbers):
    a = numbers[13]
    b = numbers[66]
    common = min(a, b)
    while common > 0:
        if a % common == 0 and b % common == 0:
            return common
        common -= 1