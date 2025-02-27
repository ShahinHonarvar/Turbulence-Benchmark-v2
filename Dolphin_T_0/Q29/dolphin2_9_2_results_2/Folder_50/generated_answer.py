def gcf_two_nums(numbers):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcf_two_nums(b, a % b)
    return gcd(numbers[90], numbers[54])