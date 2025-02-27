def gcf_three_nums(int_list):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    a = int_list[876]
    b = int_list[203]
    c = int_list[100]
    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    return gcf_abc