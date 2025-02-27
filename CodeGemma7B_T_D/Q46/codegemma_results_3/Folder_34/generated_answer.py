def gcf_three_nums(lst):

    def gcd(a, b):
        return b if a == 0 else gcd(b % a, a)
    num_1 = lst[53]
    num_2 = lst[23]
    num_3 = lst[45]
    return gcd(num_1, gcd(num_2, num_3))