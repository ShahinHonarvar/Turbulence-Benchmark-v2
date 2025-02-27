def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 56:
        return gcd(nums[56], nums[54])
    return None