def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_of_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf_of_three(numbers[37], numbers[30], numbers[48])