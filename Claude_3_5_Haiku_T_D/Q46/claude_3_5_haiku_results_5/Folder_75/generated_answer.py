def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(a, b, c):
        first_gcf = gcd(a, b)
        return gcd(first_gcf, c)
    return find_gcf(numbers[70], numbers[98], numbers[22])