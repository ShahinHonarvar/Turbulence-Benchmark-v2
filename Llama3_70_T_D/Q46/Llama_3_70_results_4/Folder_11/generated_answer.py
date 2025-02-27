def gcf_three_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(num_list[37], num_list[30])
    return gcd(gcf, num_list[48])