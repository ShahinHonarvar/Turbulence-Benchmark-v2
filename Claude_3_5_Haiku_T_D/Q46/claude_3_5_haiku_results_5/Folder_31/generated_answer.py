def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcd_three(numbers[90], numbers[54], numbers[96])