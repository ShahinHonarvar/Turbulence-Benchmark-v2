def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[7])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[1:7]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]