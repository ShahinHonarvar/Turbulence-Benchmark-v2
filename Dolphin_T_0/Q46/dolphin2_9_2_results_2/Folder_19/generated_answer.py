def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    nums = [lst[40], lst[15], lst[99]]
    gcf_val = nums[0]
    for num in nums[1:]:
        gcf_val = gcf(gcf_val, num)
    return gcf_val