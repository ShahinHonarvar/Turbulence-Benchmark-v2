def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    present = set(nums[57:86])
    total_sum = sum((n for n in range(a + 1, b) if n not in present))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]