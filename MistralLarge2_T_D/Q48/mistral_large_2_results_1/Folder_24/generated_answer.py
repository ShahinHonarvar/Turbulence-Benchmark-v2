def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[13:92]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]