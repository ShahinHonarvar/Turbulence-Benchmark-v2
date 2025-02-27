def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in nums[61:90]:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]