def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[8]
    range_nums = set(nums[3:8])
    target_nums = {i for i in range(a + 1, b)}
    missing_nums = target_nums - range_nums
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]