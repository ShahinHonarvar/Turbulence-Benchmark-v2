def return_binary_or_hexa(nums):
    a, b = (nums[42], nums[87])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[42:88]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]