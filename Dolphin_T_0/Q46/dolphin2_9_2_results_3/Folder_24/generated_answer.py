def gcf_three_nums(lst):
    nums = [lst[18], lst[37], lst[43]]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(nums[0], gcf(nums[1], nums[2]))