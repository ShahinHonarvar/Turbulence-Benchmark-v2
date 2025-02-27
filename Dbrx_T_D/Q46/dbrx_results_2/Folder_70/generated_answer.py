def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums_to_consider = [nums[990], nums[671], nums[711]]
    return gcd(nums_to_consider[0], gcd(nums_to_consider[1], nums_to_consider[2]))