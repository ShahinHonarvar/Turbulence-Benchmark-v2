def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    missing_nums_sum = sum((i for i in range(a + 1, b) if i not in nums[35:70]))
    if missing_nums_sum == 0:
        return ''
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]