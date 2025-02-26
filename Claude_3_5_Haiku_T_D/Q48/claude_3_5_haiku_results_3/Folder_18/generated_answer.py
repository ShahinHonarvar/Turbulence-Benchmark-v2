def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    missing = set(range(a + 1, b))
    for x in nums[56:91]:
        if x in missing:
            missing.remove(x)
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]