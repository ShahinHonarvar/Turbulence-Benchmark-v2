def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[200]
    existing_set = set(nums[70:201])
    total_sum = sum((x for x in range(a + 1, b) if x not in existing_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]