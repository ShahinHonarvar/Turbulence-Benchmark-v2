def return_binary_or_hexa(nums):
    if len(nums) < 98:
        return ''
    a = nums[90]
    b = nums[97]
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[91:98]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]