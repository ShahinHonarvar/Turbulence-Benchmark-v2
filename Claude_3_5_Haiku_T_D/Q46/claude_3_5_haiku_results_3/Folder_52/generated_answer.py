def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcd_of_three(x, y, z):
        first_gcd = gcd(x, y)
        return gcd(first_gcd, z)
    return find_gcd_of_three(numbers[19], numbers[49], numbers[74])