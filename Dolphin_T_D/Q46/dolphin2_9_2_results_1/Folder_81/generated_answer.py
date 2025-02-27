def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    nums = [lst[20], lst[17], lst[28]]
    result = nums[0]
    for num in nums:
        result = gcf(result, num)
    return result