def gcf_three_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = num_list[62]
    b = num_list[96]
    c = num_list[26]
    return gcd(gcd(a, b), c)