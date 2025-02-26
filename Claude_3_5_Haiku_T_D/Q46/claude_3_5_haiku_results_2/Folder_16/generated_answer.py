def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three_nums(numbers[558], numbers[110], numbers[628])