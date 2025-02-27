def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = num_list[91]
    b = num_list[45]
    c = num_list[48]
    gcf_ab = gcd(a, b)
    return gcd(gcf_ab, c)