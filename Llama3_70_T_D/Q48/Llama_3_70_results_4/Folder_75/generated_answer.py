def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[51]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[20:52]]
    total = sum(missing_nums)
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]