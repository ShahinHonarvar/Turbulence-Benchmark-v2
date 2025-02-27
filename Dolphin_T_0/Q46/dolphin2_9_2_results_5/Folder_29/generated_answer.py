def gcf_three_nums(lst):
    nums = [lst[22], lst[97], lst[64]]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    gcf = nums[0]
    for i in range(1, len(nums)):
        gcf = gcd(gcf, nums[i])
    return gcf