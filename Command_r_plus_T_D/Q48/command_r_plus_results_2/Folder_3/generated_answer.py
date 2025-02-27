def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[56], nums[88])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(nums[57:88])
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()