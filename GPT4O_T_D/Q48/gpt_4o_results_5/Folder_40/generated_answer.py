def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[3]
    sum_value = sum((x for x in range(a + 1, b) if x not in nums[:4]))
    if sum_value == 0:
        return ''
    if sum_value % 2 == 0:
        return hex(sum_value)[2:]
    else:
        return bin(sum_value)[2:]