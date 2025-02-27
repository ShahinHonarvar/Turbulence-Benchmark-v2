def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[86:100]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()