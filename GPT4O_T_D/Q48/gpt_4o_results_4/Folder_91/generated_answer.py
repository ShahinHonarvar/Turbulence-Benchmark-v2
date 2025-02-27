def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[6]
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[0:7]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]