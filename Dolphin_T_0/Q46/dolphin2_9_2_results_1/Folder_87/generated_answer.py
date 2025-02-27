def gcf_three_nums(n_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums = n_list[74:75] + n_list[60:61] + n_list[28:29]
    return gcd(nums[0], gcd(nums[1], nums[2]))