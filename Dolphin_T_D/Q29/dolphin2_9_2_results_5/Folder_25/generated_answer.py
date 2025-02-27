def gcf_two_nums(nums_list):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(nums_list[41], nums_list[69])