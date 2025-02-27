def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[57:86]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]