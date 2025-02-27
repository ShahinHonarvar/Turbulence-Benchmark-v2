def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[20:33]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]