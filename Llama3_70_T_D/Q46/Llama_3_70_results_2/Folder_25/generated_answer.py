def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(num_list[32], num_list[54])
    gcf = gcd(gcf, num_list[13])
    return gcf