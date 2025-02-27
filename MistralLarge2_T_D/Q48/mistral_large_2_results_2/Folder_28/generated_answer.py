def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[87:99]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:].upper()