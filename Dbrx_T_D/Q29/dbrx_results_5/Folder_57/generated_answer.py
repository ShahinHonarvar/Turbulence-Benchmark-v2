def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return lcm(numbers[28], numbers[49]) if numbers[28] != numbers[49] else numbers[28]