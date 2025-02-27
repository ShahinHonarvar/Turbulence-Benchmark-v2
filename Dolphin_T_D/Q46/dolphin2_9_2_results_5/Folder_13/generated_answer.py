def gcf_three_nums(nums):
    list_nums = [nums[991], nums[244], nums[974]]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_value = list_nums[0]
    for num in list_nums[1:]:
        gcf_value = gcf(gcf_value, num)
    return gcf_value