def gcf_two_nums(nums):

    def get_gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    index1 = 634
    index2 = 585
    num1 = nums[index1]
    num2 = nums[index2]
    return get_gcf(num1, num2)