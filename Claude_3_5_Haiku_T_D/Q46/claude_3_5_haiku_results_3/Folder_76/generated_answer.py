def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(a, b, c):
        first_gcd = gcd(a, b)
        return gcd(first_gcd, c)
    return gcf_multiple(numbers[876], numbers[203], numbers[100])