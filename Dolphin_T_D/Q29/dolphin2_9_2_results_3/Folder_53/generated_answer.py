def gcf_two_nums(num_list):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(num_list[28], num_list[67])