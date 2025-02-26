def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_multiple(numbers[912], numbers[170], numbers[500])