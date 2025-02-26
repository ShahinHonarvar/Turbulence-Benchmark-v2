def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (numbers[40], numbers[15], numbers[99])
    first_gcd = gcd(a, b)
    return gcd(first_gcd, c)