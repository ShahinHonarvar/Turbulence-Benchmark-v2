def gcf_three_nums(numbers):
    a = numbers[87]
    b = numbers[20]
    c = numbers[36]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return gcd(gcd(a, b), c)