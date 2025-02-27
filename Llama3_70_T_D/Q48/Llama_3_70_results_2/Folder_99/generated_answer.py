def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    total = sum((i for i in range(a + 1, b) if i not in nums[427:670]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]