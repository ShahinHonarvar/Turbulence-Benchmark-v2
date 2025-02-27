def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[48:77]))
    if not missing_sum:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]