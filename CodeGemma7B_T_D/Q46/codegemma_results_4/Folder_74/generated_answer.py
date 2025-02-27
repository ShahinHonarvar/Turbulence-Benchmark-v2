def gcd(a, b):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(a, gcd(b, c))