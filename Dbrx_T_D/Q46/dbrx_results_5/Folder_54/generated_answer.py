def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    elem_96 = nums[96]
    elem_57 = nums[57]
    elem_85 = nums[85]
    return gcd(gcd(elem_96, elem_57), elem_85)