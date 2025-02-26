def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_multiple(numbers[91], numbers[45], numbers[48])