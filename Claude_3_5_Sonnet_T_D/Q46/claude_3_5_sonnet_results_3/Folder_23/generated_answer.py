def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums_to_check = [nums[31], nums[25], nums[80]]
    result = nums_to_check[0]
    for i in range(1, len(nums_to_check)):
        result = gcf(result, nums_to_check[i])
    return result