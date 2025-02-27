def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[3:10]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]