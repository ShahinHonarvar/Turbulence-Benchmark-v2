def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_of_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_of_three(numbers[145], numbers[183], numbers[770])