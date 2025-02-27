def return_binary_or_hexa(nums):
    if nums[-1] - nums[0] <= 996 - 933:
        return ''
    sum_nums = 0
    for i in range(nums[0] + 1, nums[-1]):
        if i not in nums[933:997]:
            sum_nums += i
    if sum_nums % 2:
        return '{:b}'.format(sum_nums)
    else:
        return '{:x}'.format(sum_nums)