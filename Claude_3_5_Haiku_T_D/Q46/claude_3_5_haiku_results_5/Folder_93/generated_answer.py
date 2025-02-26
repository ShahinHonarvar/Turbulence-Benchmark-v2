def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three_nums(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three_nums(num_list[25], num_list[76], num_list[57])