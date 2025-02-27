def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[200]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[70:201]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]