def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[7]
    excluded_nums = set(nums[6:8])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in excluded_nums:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]