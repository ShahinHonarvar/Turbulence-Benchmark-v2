def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[86:100]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]