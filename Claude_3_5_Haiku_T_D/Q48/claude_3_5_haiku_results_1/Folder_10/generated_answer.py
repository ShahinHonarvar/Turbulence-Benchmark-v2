def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    missing_nums_sum = 0
    for num in range(a + 1, b):
        if num not in nums[36:55]:
            missing_nums_sum += num
    if missing_nums_sum == 0:
        return ''
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]