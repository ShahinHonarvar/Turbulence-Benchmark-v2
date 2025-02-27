def return_binary_or_hexa(nums):
    a_idx, b_idx = (62, 96)
    a, b = (nums[a_idx], nums[b_idx])
    present_numbers = set(nums[a_idx + 1:b_idx])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]