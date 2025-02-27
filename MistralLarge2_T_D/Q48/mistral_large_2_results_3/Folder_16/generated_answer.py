def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[97]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[90:98]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]