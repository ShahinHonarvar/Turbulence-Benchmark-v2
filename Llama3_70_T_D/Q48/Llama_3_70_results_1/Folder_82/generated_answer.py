def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[200]
    sum_val = sum((i for i in range(a + 1, b) if i not in nums[20:201]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 != 0:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]