def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in nums[57:85]:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]