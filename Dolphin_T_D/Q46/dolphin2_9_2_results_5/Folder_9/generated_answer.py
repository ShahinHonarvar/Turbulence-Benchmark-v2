def gcf_three_nums(nums_list):
    nums = [nums_list[66], nums_list[90], nums_list[27]]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[0], gcd(nums[1], nums[2]))