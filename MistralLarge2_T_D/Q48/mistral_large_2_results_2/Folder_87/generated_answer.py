def return_binary_or_hexa(nums):
    a, b = (nums[20], nums[43])
    target_set = set(nums[20:44])
    total_sum = sum((x for x in range(a + 1, b) if x not in target_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]