def gcf_two_nums(int_list):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(int_list[42], int_list[25])