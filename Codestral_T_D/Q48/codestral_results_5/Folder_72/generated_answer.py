def return_binary_or_hexa(nums):
    a, b = (nums[13], nums[70])
    missing_sum = sum(range(a + 1, b)) - sum(nums[14:70])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]