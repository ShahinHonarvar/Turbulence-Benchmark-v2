def gcf_three_nums(numbers):
    a = numbers[66]
    b = numbers[90]
    c = numbers[27]

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)
    return gcd(lcm(a, b), c)