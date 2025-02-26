def gcf_two_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[96]
    num2 = nums[32]
    return gcf(num1, num2)