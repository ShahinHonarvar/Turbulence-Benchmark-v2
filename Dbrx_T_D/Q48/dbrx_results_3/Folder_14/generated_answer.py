def return_binary_or_hexa(nums):
    non_present_nums = [i for i in range(nums[2] + 1, nums[5] - 1) if i not in nums]
    if not non_present_nums:
        return ''
    sum_of_non_present = sum(non_present_nums)
    if sum_of_non_present % 2:
        return format(sum_of_non_present, '#013b')[2:]
    else:
        return format(sum_of_non_present, '#x').upper()