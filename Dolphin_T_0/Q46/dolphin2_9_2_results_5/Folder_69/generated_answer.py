def gcf_three_nums(nums):

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    nums = nums[404:518]
    gcf_val = nums[0]
    for num in nums[1:]:
        gcf_val = gcf(gcf_val, num)
    return gcf_val