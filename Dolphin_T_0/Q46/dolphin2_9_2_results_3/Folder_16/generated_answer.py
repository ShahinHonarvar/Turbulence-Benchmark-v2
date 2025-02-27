def gcf_three_nums(nums):

    def gcf_two_nums(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return gcf_two_nums(a - b, b)
        return gcf_two_nums(a, b - a)
    return gcf_two_nums(gcf_two_nums(nums[558], nums[110]), nums[628])