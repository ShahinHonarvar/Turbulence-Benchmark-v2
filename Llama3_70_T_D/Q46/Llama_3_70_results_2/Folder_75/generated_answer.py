def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(num_list[70], num_list[98])
    return gcd(gcf, num_list[22])