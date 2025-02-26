def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf_three(numbers[4], numbers[1], numbers[7])