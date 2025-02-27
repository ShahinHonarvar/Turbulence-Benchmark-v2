def return_binary_or_hexa(nums):
    a, b = (nums[81], nums[86])
    total = 0
    for i in range(a + 1, b):
        if i not in nums:
            total += i
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]