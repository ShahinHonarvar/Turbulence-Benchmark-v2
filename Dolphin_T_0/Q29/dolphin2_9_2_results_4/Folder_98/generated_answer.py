def gcf_two_nums(nums_list):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(nums_list[0], nums_list[9])