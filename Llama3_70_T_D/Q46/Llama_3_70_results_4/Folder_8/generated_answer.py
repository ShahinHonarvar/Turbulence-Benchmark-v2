def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(num_list[99], num_list[28])
    return gcd(gcf, num_list[53])