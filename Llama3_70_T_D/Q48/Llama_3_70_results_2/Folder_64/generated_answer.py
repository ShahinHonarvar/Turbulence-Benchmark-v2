def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[5])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[:6]))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]