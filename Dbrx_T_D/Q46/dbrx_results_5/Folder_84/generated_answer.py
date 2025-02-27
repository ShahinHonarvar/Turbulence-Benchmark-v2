def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums_to_consider = [nums[695], nums[710], nums[914]]
    gcf = nums_to_consider[0]
    for num in nums_to_consider[1:]:
        gcf = gcd(gcf, num)
    return gcf