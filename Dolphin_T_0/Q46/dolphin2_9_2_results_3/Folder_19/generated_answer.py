def gcf_three_nums(lst):
    nums = [lst[40], lst[15], lst[99]]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = nums[0]
    num2 = nums[1]
    gcf_value = gcf(num1, num2)
    for num in nums[2:]:
        gcf_value = gcf(gcf_value, num)
    return gcf_value