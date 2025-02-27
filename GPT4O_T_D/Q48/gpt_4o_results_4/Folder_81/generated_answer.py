def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    all_nums = set(range(a + 1, b))
    present_nums = set(nums[11:100])
    missing_nums = all_nums - present_nums
    total_sum = sum(missing_nums)
    if not missing_nums:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]