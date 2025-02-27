def return_binary_or_hexa(nums):
    if not nums[110] < nums[348]:
        return ''
    if nums[-1] <= nums[110]:
        return ''
    sum_of_missing_nums = sum((num for num in range(nums[110] + 1, nums[-1]) if num not in nums))
    if sum_of_missing_nums % 2 == 0:
        return hex(sum_of_missing_nums)[2:]
    return bin(sum_of_missing_nums)[2:]