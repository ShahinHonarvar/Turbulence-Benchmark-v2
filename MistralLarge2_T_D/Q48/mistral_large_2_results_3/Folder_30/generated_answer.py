def return_binary_or_hexa(nums):
    a, b = (nums[22], nums[24])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[22:25]))
    if not missing_sum:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]