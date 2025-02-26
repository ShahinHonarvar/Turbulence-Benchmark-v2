def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_of_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_of_three(numbers[91], numbers[45], numbers[48])