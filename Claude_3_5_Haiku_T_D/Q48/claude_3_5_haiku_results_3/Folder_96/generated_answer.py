def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[200]
    missing = set(range(a + 1, b))
    for num in nums[50:201]:
        if num in missing:
            missing.remove(num)
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]