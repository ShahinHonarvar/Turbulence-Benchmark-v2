def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums_list = [nums[87], nums[20], nums[36]]
    result = nums_list[0]
    i = 1
    while i < len(nums_list):
        result = gcf(result, nums_list[i])
        i += 1
    return result