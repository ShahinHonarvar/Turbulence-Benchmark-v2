def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcd_three(num_list[637], num_list[411], num_list[757])