def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    if all((i in nums for i in range(a + 1, b))):
        return ''
    result_sum = sum((i for i in range(a + 1, b) if i not in nums))
    if result_sum % 2 == 0:
        return hex(result_sum)[2:]
    else:
        return bin(result_sum)[2:]