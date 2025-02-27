def gcf_two_nums(nums_list):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(nums_list[47], nums_list[22])