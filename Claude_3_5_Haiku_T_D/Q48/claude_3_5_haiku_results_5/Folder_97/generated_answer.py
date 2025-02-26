def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    if a + 1 >= b:
        return ''
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[34:70]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]