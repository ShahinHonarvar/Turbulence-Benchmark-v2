def return_binary_or_hexa(nums):
    a, b = (nums[29], nums[53])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in nums[29:54]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()