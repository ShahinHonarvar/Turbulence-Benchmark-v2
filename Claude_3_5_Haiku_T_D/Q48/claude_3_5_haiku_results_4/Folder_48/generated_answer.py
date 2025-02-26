def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    total_sum = 0
    present_nums = set(nums[933:997])
    for num in range(a + 1, b):
        if num not in present_nums:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]