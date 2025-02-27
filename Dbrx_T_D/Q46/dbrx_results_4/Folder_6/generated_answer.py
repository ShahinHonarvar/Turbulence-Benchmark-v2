def gcf_three_nums(numbers):
    a = 93
    b = 94
    c = 57
    num1 = numbers[a]
    num2 = numbers[b]
    num3 = numbers[c]

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)
    factor = lcm(num1, num2)
    factor = gcd(factor, num3)
    return factor