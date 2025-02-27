def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[51:93]]
    total = sum(missing_nums)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]