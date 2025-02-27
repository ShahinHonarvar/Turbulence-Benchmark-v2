def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums_to_consider = [nums[19], nums[94], nums[78]]
    return gcd(nums_to_consider[0], gcd(nums_to_consider[1], nums_to_consider[2]))