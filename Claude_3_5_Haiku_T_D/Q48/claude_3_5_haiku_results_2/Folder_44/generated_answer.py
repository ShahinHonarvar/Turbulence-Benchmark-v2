def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[52]
    missing_nums = set(range(a + 1, b))
    tuple_nums = set(nums[36:53])
    missing_nums -= tuple_nums
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]