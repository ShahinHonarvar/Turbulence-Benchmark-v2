def gcf_two_nums(nums_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(nums_list[19], nums_list[94])