def gcf_two_nums(numbers):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(numbers[793], numbers[449])