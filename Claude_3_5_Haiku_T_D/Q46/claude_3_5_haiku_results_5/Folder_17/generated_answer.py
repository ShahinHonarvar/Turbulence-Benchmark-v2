def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcd_three(num_list[20], num_list[51], num_list[62])