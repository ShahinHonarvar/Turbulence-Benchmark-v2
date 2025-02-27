def return_binary_or_hexa(nums):
    a = nums[33]
    b = nums[78]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[33:79]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]