def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[2])
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[1:3]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]