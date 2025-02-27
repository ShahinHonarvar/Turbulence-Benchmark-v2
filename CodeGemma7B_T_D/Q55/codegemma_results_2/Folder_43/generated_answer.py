def lists_with_product_equal_n(nums):
    circular_nums = nums + nums[0:len(nums) - 1]
    first = 0
    sublists = []
    for second in range(len(circular_nums)):
        if circular_nums[first] * circular_nums[second] == -26:
            sublists.append(circular_nums[first:second + 1])
            first = second + 1
        elif circular_nums[first] * circular_nums[second] > -26:
            first = second + 1
    return sublists