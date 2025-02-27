def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    missing_sum = sum(range(a + 1, b)) - sum(nums[32 + 1:44])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]