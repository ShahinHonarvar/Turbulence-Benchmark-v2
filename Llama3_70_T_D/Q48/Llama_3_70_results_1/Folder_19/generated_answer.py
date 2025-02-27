def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    missing_nums = set(range(a + 1, b)).difference(nums[1:5])
    total = sum(missing_nums)
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]