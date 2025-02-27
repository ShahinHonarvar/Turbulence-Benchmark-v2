def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums_to_consider = [nums[24], nums[25], nums[80]]
    return gcd(gcd(nums_to_consider[0], nums_to_consider[1]), nums_to_consider[2])