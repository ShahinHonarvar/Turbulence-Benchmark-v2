def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[5]
    sum_val = sum((i for i in range(a + 1, b) if i not in nums[:6]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]