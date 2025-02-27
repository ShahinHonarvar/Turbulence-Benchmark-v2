def gcf_two_nums(num_list):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(num_list[87], num_list[95])