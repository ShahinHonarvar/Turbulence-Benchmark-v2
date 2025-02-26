def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_multiple(numbers[76], numbers[35], numbers[74])