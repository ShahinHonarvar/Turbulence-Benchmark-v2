def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_numbers(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three_numbers(numbers[24], numbers[45], numbers[38])