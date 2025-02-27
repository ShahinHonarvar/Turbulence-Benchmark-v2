def gcf_two_nums(numbers):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(numbers[166], numbers[106])