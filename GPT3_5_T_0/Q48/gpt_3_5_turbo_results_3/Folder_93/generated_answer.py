def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in nums[57:86]:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]