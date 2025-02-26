def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        first_gcd = gcd(x, y)
        return gcd(first_gcd, z)
    return gcd_three_nums(numbers[19], numbers[49], numbers[74])