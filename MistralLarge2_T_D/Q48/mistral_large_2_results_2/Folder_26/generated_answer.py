def return_binary_or_hexa(nums):
    a, b = (nums[68], nums[99])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[68:100]))
    if not missing_sum:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]