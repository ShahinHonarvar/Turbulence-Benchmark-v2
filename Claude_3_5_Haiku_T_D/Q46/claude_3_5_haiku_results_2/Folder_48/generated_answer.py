def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(x, y, z):
        first_gcf = gcd(x, y)
        return gcd(first_gcf, z)
    return find_gcf(numbers[654], numbers[312], numbers[441])