def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[3])
    present_nums = set(nums[0:4])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in present_nums:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]