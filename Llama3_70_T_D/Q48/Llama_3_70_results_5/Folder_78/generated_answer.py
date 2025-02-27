def return_binary_or_hexa(nums):
    a = nums[62]
    b = nums[96]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[62:97]]
    total = sum(missing_nums)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]