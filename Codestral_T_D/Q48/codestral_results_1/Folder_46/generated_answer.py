def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[79]
    missing_sum = sum(range(a + 1, b)) - sum(nums[10:79])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]