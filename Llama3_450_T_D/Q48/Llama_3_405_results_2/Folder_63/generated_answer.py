def return_binary_or_hexa(nums):
    a = nums[81]
    b = nums[86]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[81:87]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]