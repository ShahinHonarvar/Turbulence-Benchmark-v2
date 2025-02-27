def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    missing_sum = sum(range(a + 1, b))
    for i in range(39, 52):
        if nums[i] >= b:
            break
        missing_sum -= nums[i]
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]