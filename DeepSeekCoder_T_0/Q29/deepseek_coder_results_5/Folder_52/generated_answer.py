def gcf_two_nums(num_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(num_list[90], num_list[41])