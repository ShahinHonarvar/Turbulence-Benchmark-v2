def gcf_two_nums(nums):
    num1 = nums[534]
    num2 = nums[630]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(num1, num2)