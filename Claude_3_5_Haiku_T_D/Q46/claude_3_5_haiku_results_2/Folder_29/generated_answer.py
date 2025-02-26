def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three(x, y, z):
        first_gcf = gcd(x, y)
        return gcd(first_gcf, z)
    return gcd_three(numbers[22], numbers[97], numbers[64])