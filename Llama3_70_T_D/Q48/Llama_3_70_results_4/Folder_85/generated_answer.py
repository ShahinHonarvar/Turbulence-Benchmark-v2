def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    sum_val = sum((i for i in range(a + 1, b) if i not in nums[1:9]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]