def return_binary_or_hexa(nums):
    a = nums[35]
    b = nums[64]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[35:65]]
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]