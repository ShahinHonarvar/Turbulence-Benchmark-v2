def gcf_two_nums(numbers):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(numbers[49], numbers[53])