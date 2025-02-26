def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf(numbers[46], numbers[84], numbers[23])