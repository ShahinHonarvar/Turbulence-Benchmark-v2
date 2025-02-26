def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    missing = []
    for x in range(a + 1, b):
        if x not in nums[27:97]:
            missing.append(x)
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]