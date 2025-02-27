def return_binary_or_hexa(nums):
    a = nums[7]
    b = nums[9]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[8:10]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]