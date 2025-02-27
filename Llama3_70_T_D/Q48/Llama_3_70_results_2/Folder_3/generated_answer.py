def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[88]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[56:89]]
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]