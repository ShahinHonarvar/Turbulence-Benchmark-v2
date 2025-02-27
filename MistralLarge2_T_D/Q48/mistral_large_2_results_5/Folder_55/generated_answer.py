def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[12])
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[10:12]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]