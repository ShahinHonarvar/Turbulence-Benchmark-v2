def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(numbers[90], numbers[84])
    gcf = gcd(gcf, numbers[47])
    return gcf