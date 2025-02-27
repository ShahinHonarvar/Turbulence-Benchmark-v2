def gcf_two_nums(integers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(integers[49], integers[53])