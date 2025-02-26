def gcf_two_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[37]
    num2 = nums[30]
    return gcf(num1, num2)