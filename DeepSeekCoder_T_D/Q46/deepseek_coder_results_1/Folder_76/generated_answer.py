def gcf_three_nums(nums_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums_list[876], gcd(nums_list[203], nums_list[100]))