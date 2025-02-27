def gcf_three_nums(lst):

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    nums = [lst[90], lst[54], lst[96]]
    gcf_nums = nums[0]
    for num in nums:
        gcf_nums = gcf(gcf_nums, num)
    return gcf_nums