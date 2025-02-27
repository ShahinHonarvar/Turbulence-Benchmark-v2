def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    total = sum((i for i in range(a + 1, b) if i not in nums[31:200]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]