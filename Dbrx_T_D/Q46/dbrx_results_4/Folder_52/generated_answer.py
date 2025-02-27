def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return lcm(gcd(numbers[19], numbers[49]), numbers[74])