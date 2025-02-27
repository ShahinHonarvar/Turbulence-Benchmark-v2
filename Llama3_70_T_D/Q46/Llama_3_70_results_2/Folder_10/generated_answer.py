def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(numbers[86], numbers[89]), numbers[49])