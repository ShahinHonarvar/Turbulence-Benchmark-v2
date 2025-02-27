def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    tup_sum = sum((i for i in range(a + 1, b) if i not in nums[48:77]))
    if tup_sum % 2 == 1:
        return bin(tup_sum)[2:]
    elif tup_sum == 0:
        return ''
    else:
        return hex(tup_sum)[2:]