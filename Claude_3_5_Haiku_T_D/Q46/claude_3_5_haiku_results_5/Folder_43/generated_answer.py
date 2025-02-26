def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three_nums(numbers[33], numbers[78], numbers[93])