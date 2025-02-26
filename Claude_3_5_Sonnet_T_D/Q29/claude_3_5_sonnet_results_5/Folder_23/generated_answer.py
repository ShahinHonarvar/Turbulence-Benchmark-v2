def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) >= 75:
        return gcd(nums[48], nums[74])
    else:
        return None