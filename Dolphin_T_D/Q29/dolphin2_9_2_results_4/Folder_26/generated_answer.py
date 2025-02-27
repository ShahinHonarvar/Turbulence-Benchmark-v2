def gcd_two_nums(numbers):
    a = numbers[49]
    b = numbers[31]
    for i in range(min(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1