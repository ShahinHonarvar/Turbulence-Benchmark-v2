def return_binary_or_hexa(nums):
    a, b = (nums[20], nums[51])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[20:52]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]