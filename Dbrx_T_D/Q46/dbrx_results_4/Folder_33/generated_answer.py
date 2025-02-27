def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a, b, c = (numbers[252], numbers[149], numbers[564])
    return gcd(a, gcd(b, c))