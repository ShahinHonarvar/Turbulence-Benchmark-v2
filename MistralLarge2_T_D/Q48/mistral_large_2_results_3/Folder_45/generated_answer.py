def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[30:201]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]