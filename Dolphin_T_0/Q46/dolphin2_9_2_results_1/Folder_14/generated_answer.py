def gcf_three_nums(lst):
    nums = [lst[17], lst[88], lst[35]]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(nums[0], gcf(nums[1], nums[2]))