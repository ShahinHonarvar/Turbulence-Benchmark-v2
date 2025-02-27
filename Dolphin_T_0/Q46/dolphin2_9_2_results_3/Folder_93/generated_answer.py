def gcf_three_nums(num_list):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(num_list[25], gcd(num_list[76], num_list[57]))