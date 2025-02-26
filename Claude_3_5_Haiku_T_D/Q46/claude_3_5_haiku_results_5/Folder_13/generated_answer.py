def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(a, b, c):
        gcf_ab = gcd(a, b)
        return gcd(gcf_ab, c)
    return find_gcf(numbers[991], numbers[244], numbers[974])